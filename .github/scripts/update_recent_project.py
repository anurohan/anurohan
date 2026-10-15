#!/usr/bin/env python3
import os
import re
import json
import base64
import math
import http.client
import urllib.request
import urllib.error
import time
from datetime import datetime, timezone


EXCLUDED_REPOSITORIES = {
    "first-contributions",
    "git-commands-",
    "daily-_leetcode",
    "daily_practice-",
    "basic-c-project",
    "basic-to-advanve-java",
    "-star_pattern_c",
    "cpp",
}
MAX_COMMIT_HISTORY = 10
DOC_COMMIT_PATTERN = re.compile(
    r"\b(?:docs?|documentation|readme|markdown|gitignore|node_modules)\b",
    re.IGNORECASE,
)

def fetch_json(url, token=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 2:
                raise RuntimeError(f"GitHub API request failed for {url}: {e}") from e
        except (urllib.error.URLError, http.client.IncompleteRead, json.JSONDecodeError) as e:
            if attempt == 2:
                raise RuntimeError(f"GitHub API request failed for {url}: {e}") from e
        time.sleep(2 ** attempt)
    raise RuntimeError(f"GitHub API request failed after retries for {url}.")

def fetch_file_content(owner, repo, path, token=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "content" in data:
                return base64.b64decode(data["content"]).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise RuntimeError(f"GitHub API request failed for {url}: {e}") from e
    return None


def is_documentation_commit(message):
    return bool(DOC_COMMIT_PATTERN.search(message))


def get_latest_project_update(username, repo_name, token=None):
    commits_url = (
        f"https://api.github.com/repos/{username}/{repo_name}/commits"
        f"?per_page={MAX_COMMIT_HISTORY}"
    )
    commits = fetch_json(commits_url, token)
    for commit in commits:
        if is_documentation_commit(commit["commit"]["message"]):
            continue
        return commit["commit"]["committer"]["date"]
    return None


def is_excluded_project(name, username):
    normalized = name.lower()
    return (
        normalized in {username.lower(), ".github"}
        or normalized in EXCLUDED_REPOSITORIES
        or normalized.startswith(("daily-", "daily_", "basic-"))
    )


def calculate_project_score(repo, project_updated_at, now=None):
    updated = datetime.fromisoformat(project_updated_at.replace("Z", "+00:00"))
    current = now or datetime.now(timezone.utc)
    age_days = max(0, (current - updated).total_seconds() / 86400)
    size_score = min(18, math.log2(repo.get("size", 0) + 1) * 2)
    quality_score = (
        size_score
        + (10 if repo.get("description") else 0)
        + (8 if repo.get("language") else 0)
        + (10 if repo.get("homepage") else 0)
        + min(6, len(repo.get("topics") or []) * 2)
        + min(12, repo.get("stargazers_count", 0) * 4)
        + min(12, repo.get("forks_count", 0) * 6)
    )
    freshness_score = max(0, 60 - age_days)
    return quality_score + freshness_score


def get_latest_project(username, token=None):
    url = f"https://api.github.com/users/{username}/repos?sort=pushed&direction=desc&per_page=100"
    repos = fetch_json(url, token)
    if not repos:
        raise RuntimeError(f"No repositories returned for GitHub user {username}.")

    candidates = []
    for repo in repos:
        name = repo.get("name", "")
        if (
            is_excluded_project(name, username)
            or repo.get("fork", False)
            or repo.get("archived", False)
            or repo.get("size", 0) <= 0
            or not repo.get("language")
        ):
            continue

        print(f"Checking project activity: {name}")
        project_updated_at = get_latest_project_update(username, name, token)
        if not project_updated_at:
            continue

        candidate = dict(repo)
        candidate["project_updated_at"] = project_updated_at
        candidate["project_score"] = calculate_project_score(repo, project_updated_at)
        candidates.append(candidate)

    if not candidates:
        raise RuntimeError(
            f"No eligible projects with recent non-documentation activity were found for {username}."
        )

    ranked = sorted(
        candidates,
        key=lambda repo: (
            repo["project_score"],
            repo["project_updated_at"],
            repo.get("pushed_at", ""),
        ),
        reverse=True,
    )
    print("Top project candidates:")
    for repo in ranked[:5]:
        print(
            f"  {repo['name']}: score {repo['project_score']:.1f}, "
            f"last project update {repo['project_updated_at']}"
        )
    return ranked[0]

def clean_title(name):
    cleaned = name.replace("-", " ").replace("_", " ").strip()
    words = cleaned.split()
    res = []
    for w in words:
        if w.lower() in ["ai", "ml", "rag", "api", "iot", "cv", "llm"]:
            res.append(w.upper())
        else:
            res.append(w.capitalize())
    return " ".join(res)


def clean_card_text(text, max_length):
    cleaned = re.sub(r"\s+", " ", re.sub(r"[*_`#]", "", text)).strip()
    if len(cleaned) <= max_length:
        return cleaned
    shortened = cleaned[: max_length - 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
    if not shortened:
        shortened = cleaned[: max_length - 1]
    return shortened + "…"


def extract_project_info(owner, repo_data, token=None):
    repo_name = repo_data["name"]
    display_title = clean_card_text(clean_title(repo_name).upper(), 26)
    html_url = repo_data["html_url"]
    homepage = repo_data.get("homepage") or ""
    desc = repo_data.get("description") or ""

    # Languages
    lang_url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
    langs_data = fetch_json(lang_url, token) or {}
    languages = list(langs_data.keys())[:4]

    # Topics
    topics = repo_data.get("topics") or []

    # Defaults
    subtitle = "Intelligent System & Software Build"
    problem = "Engineering intelligent workflows and real-world system applications."
    feature = "Built with high performance and modular design."
    stack = " · ".join(languages) if languages else "Python · TypeScript"

    # Specific smart extraction for known repositories or reading README
    if repo_name.lower() == "hospital":
        subtitle = "Hospital Appointment and Patient Management"
        problem = "Streamlining patient services and appointment workflows for a nursing hospital."
        feature = clean_card_text(desc, 100)
    elif repo_name.lower() == "osho-ai":
        subtitle = "Retrieval-Augmented Generation (RAG) System"
        problem = "Contextual question-answering with semantic passage retrieval over vector database."
        stack = "Python · TypeScript · FAISS · Ollama · Sentence Transformers · RAG"
        feature = "Conversational AI companion matching user queries against indexed discourse vectors."
        homepage = "https://frontend-phi-topaz-18.vercel.app/"
    elif repo_name.lower() == "lifelens-ai":
        subtitle = "Multimodal Personal Knowledge System"
        problem = "Personal information is scattered across formats and hard to organize or retrieve."
        stack = "Python · Next.js · FastAPI · PostgreSQL · pgvector · Sentence Transformers"
        feature = "Processes, organizes and semantically retrieves personal information in real time."
        if not homepage:
            homepage = "https://lifelens-ai-nine.vercel.app"
    else:
        # Check README if desc is empty
        if not desc:
            readme_text = fetch_file_content(owner, repo_name, "README.md", token)
            if not readme_text:
                readme_text = fetch_file_content(owner, repo_name, "app/README.md", token)
            if readme_text:
                lines = [line.strip() for line in readme_text.splitlines() if line.strip() and not line.startswith("#")]
                if lines:
                    desc = lines[0][:120]
        
        if desc:
            subtitle = clean_card_text(desc, 82)
            feature = clean_card_text(desc, 100)
        if topics:
            stack = " · ".join([t.capitalize() for t in topics[:5]]) + (" · " + " · ".join(languages[:3]) if languages else "")

    return {
        "name": repo_name,
        "title": display_title,
        "subtitle": subtitle,
        "problem": problem,
        "stack": stack,
        "feature": feature,
        "html_url": html_url,
        "homepage": homepage if homepage.startswith("http") else "",
        "project_updated_at": repo_data["project_updated_at"],
    }

def generate_svg(info):
    title = info["title"]
    subtitle = info["subtitle"]
    problem = info["problem"]
    stack = info["stack"]
    feature = info["feature"]

    def esc(text):
        return (text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace('"', "&quot;"))

    svg = f"""    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 250" width="1000" height="250" role="img" aria-label="Featured Project — {esc(title)}">
<defs>
<style>
.m{{font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,'DejaVu Sans Mono',monospace}}
.s{{font-family:'Segoe UI',Helvetica,Arial,sans-serif}}
.blink{{animation:b 1.4s infinite}}
@keyframes b{{0%,49%{{opacity:1}}50%,100%{{opacity:0.2}}}}
</style>
<linearGradient id="sw"><stop offset="0" stop-color="#4fd8ff" stop-opacity="0"/><stop offset=".5" stop-color="#4fd8ff"/><stop offset="1" stop-color="#4fd8ff" stop-opacity="0"/></linearGradient>
</defs>
<rect x=".5" y=".5" width="999" height="249" rx="12" fill="#070b12" stroke="#16283a"/>
<text class="s" x="975" y="225" text-anchor="end" font-size="190" font-weight="800" fill="#0b1520">NEW</text>
<rect width="5" height="250" rx="2" fill="#4fd8ff"><animate attributeName="opacity" values=".4;1;.4" dur="3s" repeatCount="indefinite"/></rect>
<rect y="0" width="140" height="2" fill="url(#sw)"><animate attributeName="x" from="-140" to="1000" dur="5s" repeatCount="indefinite"/></rect>

<circle class="blink" cx="48" cy="42" r="4.5" fill="#3ddc97"/>
<text class="m" x="62" y="46" font-size="12" letter-spacing="4" fill="#4fd8ff">FEATURED PROJECT</text>
<text class="m" x="960" y="46" text-anchor="end" font-size="11" letter-spacing="3" fill="#3ddc97">● PROJECT QUALITY / RECENT ACTIVITY</text>

<text class="s" x="40" y="96" font-size="38" font-weight="800" fill="#e6edf3">{esc(title)}</text>
<text class="s" x="40" y="124" font-size="17" fill="#8b9bab">{esc(subtitle)}</text>
<line x1="40" y1="142" x2="960" y2="142" stroke="#16283a"/>
<g class="m" font-size="13">
<text x="40" y="170" fill="#4fd8ff" fill-opacity=".8">PROBLEM</text><text x="130" y="170" fill="#c9d1d9">{esc(problem)}</text>
<text x="40" y="194" fill="#4fd8ff" fill-opacity=".8">STACK</text><text x="130" y="194" fill="#c9d1d9">{esc(stack)}</text>
<text x="40" y="218" fill="#4fd8ff" fill-opacity=".8">FEATURE</text><text x="130" y="218" fill="#c9d1d9">{esc(feature)}</text>
</g>
</svg>
"""
    return svg.lstrip()

def update_readme(info, readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    target_url = info.get("homepage") if info.get("homepage") else info["html_url"]
    
    demo_button = ""
    if info.get("homepage"):
        demo_button = f'<a href="{info["homepage"]}"><img src="https://img.shields.io/badge/LIVE_DEMO-%E2%86%92-4fd8ff?style=for-the-badge&labelColor=0b1118" alt="Live Demo"/></a>\n&nbsp;\n'

    source_button = f'<a href="{info["html_url"]}"><img src="https://img.shields.io/badge/SOURCE_CODE-%3C%2F%3E-4fd8ff?style=for-the-badge&labelColor=0b1118" alt="Source code"/></a>'

    # Cache buster query string using current unix timestamp or version
    update_time = datetime.fromisoformat(info["project_updated_at"].replace("Z", "+00:00"))
    v_param = f"v={int(update_time.timestamp())}"

    new_section = f"""<!-- RECENT-PROJECT-START -->
<div align="center">

<a href="{target_url}">
  <img src="./assets/recent-project.svg?{v_param}" alt="Featured Project — {info['title']}" width="100%"/>
</a>

<br/><br/>

{demo_button}{source_button}

</div>
<!-- RECENT-PROJECT-END -->"""

    pattern = r"<!-- RECENT-PROJECT-START -->[\s\S]*?<!-- RECENT-PROJECT-END -->"
    if re.search(pattern, content):
        content = re.sub(pattern, new_section, content)
    else:
        old_screen04 = r'<h2 align="center" id="recently-developed">(?:RECENTLY DEVELOPED PROJECT|FEATURED PROJECT — QUALITY \+ RECENCY)</h2>[\s\S]*?<img src="\./assets/divider\.svg" width="100%" alt=""/>'
        replacement = f"""<h2 align="center" id="recently-developed">FEATURED PROJECT — QUALITY + RECENCY</h2>

{new_section}

<img src="./assets/divider.svg" width="100%" alt=""/>"""
        content = re.sub(old_screen04, replacement, content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    username = os.environ.get("GITHUB_REPOSITORY_OWNER", "anurohan")
    token = os.environ.get("GITHUB_TOKEN")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    print(f"Ranking active project repositories for user: {username}")
    selected_repo = get_latest_project(username, token)
    print(
        f"Selected {selected_repo['name']} "
        f"(score: {selected_repo['project_score']:.1f}, "
        f"last project update: {selected_repo['project_updated_at']})"
    )
    info = extract_project_info(username, selected_repo, token)
    print(f"Generated card for {info['title']} | Repo: {info['html_url']}")

    # 1. Update SVG
    svg_content = generate_svg(info)
    svg_path = os.path.join(repo_root, "assets", "recent-project.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Updated {svg_path}")

    # 2. Update README.md
    readme_path = os.path.join(repo_root, "README.md")
    update_readme(info, readme_path)
    print(f"Updated {readme_path}")

if __name__ == "__main__":
    main()
