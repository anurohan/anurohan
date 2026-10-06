#!/usr/bin/env python3
import os
import re
import json
import base64
import urllib.request
import urllib.error

def fetch_json(url, token=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

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
    except Exception:
        pass
    return None

def get_latest_project(username, token=None):
    url = f"https://api.github.com/users/{username}/repos?sort=pushed&direction=desc&per_page=30"
    repos = fetch_json(url, token)
    if not repos:
        return None
    
    # Filter out profile repo, forks, and special repos
    filtered = []
    for r in repos:
        name = r.get("name", "")
        if name.lower() in [username.lower(), ".github"]:
            continue
        if r.get("fork", False):
            continue
        filtered.append(r)
    
    if not filtered:
        return None
    
    return filtered[0]

def clean_title(name):
    # e.g. osho-ai -> OSHO AI, lifelens-ai -> LIFELENS AI
    cleaned = name.replace("-", " ").replace("_", " ").strip()
    words = cleaned.split()
    res = []
    for w in words:
        if w.lower() in ["ai", "ml", "rag", "api", "iot", "cv", "llm"]:
            res.append(w.upper())
        else:
            res.append(w.capitalize())
    return " ".join(res)

def extract_project_info(owner, repo_data, token=None):
    repo_name = repo_data["name"]
    display_title = clean_title(repo_name).upper()
    html_url = repo_data["html_url"]
    homepage = repo_data.get("homepage") or ""
    desc = repo_data.get("description") or ""

    # Languages
    lang_url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
    langs_data = fetch_json(lang_url, token) or {}
    languages = list(langs_data.keys())[:4]

    # Topics
    topics = repo_data.get("topics") or []

    # If description is missing, inspect repo for context
    subtitle = "Intelligent System & Software Build"
    problem = "Engineering intelligent workflows and real-world system applications."
    feature = "Built with high performance and modular design."
    stack = " · ".join(languages) if languages else "Python · TypeScript"

    # Specific smart extraction for known repositories or reading README
    if repo_name.lower() == "osho-ai":
        subtitle = "Retrieval-Augmented Generation (RAG) System"
        problem = "Contextual question-answering with semantic passage retrieval over vector database."
        stack = "Python · TypeScript · FAISS · Ollama · Sentence Transformers · RAG"
        feature = "Conversational AI companion matching user queries against indexed discourse vectors."
    elif repo_name.lower() == "lifelens-ai":
        subtitle = "Multimodal Personal Knowledge System"
        problem = "Personal information is scattered across formats and hard to organize or retrieve."
        stack = "Python · Next.js · FastAPI · PostgreSQL · pgvector · Sentence Transformers"
        feature = "Processes, organizes and semantically retrieves personal information in real time."
    else:
        # Check README if desc is empty
        if not desc:
            readme_text = fetch_file_content(owner, repo_name, "README.md", token)
            if not readme_text:
                readme_text = fetch_file_content(owner, repo_name, "app/README.md", token)
            if readme_text:
                # Find first non-header non-empty line
                lines = [line.strip() for line in readme_text.splitlines() if line.strip() and not line.startswith("#")]
                if lines:
                    desc = lines[0][:120]
        
        if desc:
            subtitle = desc[:70]
            feature = desc[:110]
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
    }

def generate_svg(info):
    title = info["title"]
    subtitle = info["subtitle"]
    problem = info["problem"]
    stack = info["stack"]
    feature = info["feature"]

    # Escape XML entities
    def esc(text):
        return (text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace('"', "&quot;"))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 250" width="1000" height="250" role="img" aria-label="Recent Project — {esc(title)}">
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
<text class="m" x="62" y="46" font-size="12" letter-spacing="4" fill="#4fd8ff">RECENTLY DEVELOPED</text>
<text class="m" x="960" y="46" text-anchor="end" font-size="11" letter-spacing="3" fill="#3ddc97">● ACTIVE BUILD / LATEST REPO</text>

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
    return svg

def update_readme(info, readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    demo_button = ""
    if info.get("homepage"):
        demo_button = f'<a href="{info["homepage"]}"><img src="https://img.shields.io/badge/LIVE_DEMO-%E2%86%92-4fd8ff?style=for-the-badge&labelColor=0b1118" alt="Live Demo"/></a>\n&nbsp;\n'

    source_button = f'<a href="{info["html_url"]}"><img src="https://img.shields.io/badge/SOURCE_CODE-%3C%2F%3E-4fd8ff?style=for-the-badge&labelColor=0b1118" alt="Source code"/></a>'

    new_section = f"""<!-- RECENT-PROJECT-START -->
<div align="center">

<img src="./assets/recent-project.svg" alt="Recently Developed — {info['title']}" width="100%"/>

{demo_button}{source_button}

</div>
<!-- RECENT-PROJECT-END -->"""

    pattern = r"<!-- RECENT-PROJECT-START -->[\s\S]*?<!-- RECENT-PROJECT-END -->"
    if re.search(pattern, content):
        content = re.sub(pattern, new_section, content)
    else:
        # If markers don't exist yet, insert them under screen 04
        old_screen04 = r'<h2 align="center" id="recently-developed">RECENTLY DEVELOPED PROJECT</h2>[\s\S]*?<img src="\./assets/divider\.svg" width="100%" alt=""/>'
        replacement = f"""<h2 align="center" id="recently-developed">RECENTLY DEVELOPED PROJECT</h2>

{new_section}

<img src="./assets/divider.svg" width="100%" alt=""/>"""
        content = re.sub(old_screen04, replacement, content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    username = os.environ.get("GITHUB_REPOSITORY_OWNER", "anurohan")
    token = os.environ.get("GITHUB_TOKEN")
    
    # Root dir of repo
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    print(f"Fetching latest repo for user: {username}")
    latest_repo = get_latest_project(username, token)
    if not latest_repo:
        print("No repository found.")
        return

    print(f"Latest repository found: {latest_repo['name']} (pushed: {latest_repo.get('pushed_at')})")
    info = extract_project_info(username, latest_repo, token)
    print(f"Extracted info: {info['title']} | Stack: {info['stack']}")

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
