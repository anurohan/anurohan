#!/usr/bin/env python3
"""
generate_dsa_hero.py
Generates the Live DSA Coding Lab animated SVG for Raushan Kumar's GitHub Profile.
- Dimensions: 1000 x 400 (viewBox="0 0 1000 400")
- 100% self-contained pure SVG + CSS keyframes (GitHub Camo & img tag compatible, 0 JS runtime)
- Multi-problem continuous cinematic execution cycle:
    1. Two Sum (HashMap)
    2. Binary Search (Divide & Conquer)
    3. Valid Parentheses (Stack LIFO)
    4. Longest Substring Without Repeating Characters (Sliding Window)
- High-tech engineering-lab aesthetic matching current profile palette
"""

import os
import json

def generate_svg():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
    problems_path = os.path.join(workspace_dir, "data", "problems.json")
    output_path = os.path.join(workspace_dir, "assets", "hero.svg")

    # Read problems data
    with open(problems_path, "r", encoding="utf-8") as f:
        all_problems = json.load(f)

    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400" width="1000" height="400" role="img" aria-label="Raushan Kumar — Live DSA Coding Lab (Java / Algorithms)">
<title>Raushan Kumar — Live DSA Coding Lab (Java / Algorithms)</title>
<defs>
<style><![CDATA[
  .mono { font-family: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace; }
  .sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif; }

  /* Blinking & Scanline */
  .blink-fast { animation: blinkAnim 1.2s infinite; }
  .blink-cursor { animation: blinkCursor 0.75s infinite; }
  @keyframes blinkAnim { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0.2; } }
  @keyframes blinkCursor { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }

  /* Horizontal Scanline */
  .scanline {
    animation: scanMove 6s linear infinite;
  }
  @keyframes scanMove {
    0% { transform: translateY(0); opacity: 0.12; }
    50% { opacity: 0.30; }
    100% { transform: translateY(352px); opacity: 0.12; }
  }

  /* Scene Transitions (Total Cycle: 48s, 12s per scene) */
  .scene { opacity: 0; pointer-events: none; }
  .scene-1 { animation: s1Timeline 48s infinite; }
  .scene-2 { animation: s2Timeline 48s infinite; }
  .scene-3 { animation: s3Timeline 48s infinite; }
  .scene-4 { animation: s4Timeline 48s infinite; }

  @keyframes s1Timeline {
    0%, 1% { opacity: 0; }
    2%, 23% { opacity: 1; }
    24.5%, 100% { opacity: 0; }
  }
  @keyframes s2Timeline {
    0%, 24% { opacity: 0; }
    25.5%, 48% { opacity: 1; }
    49.5%, 100% { opacity: 0; }
  }
  @keyframes s3Timeline {
    0%, 49% { opacity: 0; }
    50.5%, 73% { opacity: 1; }
    74.5%, 100% { opacity: 0; }
  }
  @keyframes s4Timeline {
    0%, 74% { opacity: 0; }
    75.5%, 98% { opacity: 1; }
    99.5%, 100% { opacity: 0; }
  }

  /* Trace & Data Flow Animations */
  .trace-pulse {
    animation: tracePulse 2s ease-in-out infinite;
  }
  @keyframes tracePulse {
    0%, 100% { stroke-opacity: 0.4; }
    50% { stroke-opacity: 1; }
  }

  .accepted-glow {
    animation: accGlow 1.6s ease-in-out infinite;
  }
  @keyframes accGlow {
    0%, 100% { filter: drop-shadow(0 0 2px #3ddc97); }
    50% { filter: drop-shadow(0 0 8px #3ddc97); }
  }

  /* Progressive Code Line Reveal (Synchronized inside 12s cycle) */
  .code-l1 { animation: codeL1 12s infinite; }
  .code-l2 { animation: codeL2 12s infinite; }
  .code-l3 { animation: codeL3 12s infinite; }
  .code-l4 { animation: codeL4 12s infinite; }
  .code-l5 { animation: codeL5 12s infinite; }
  .code-l6 { animation: codeL6 12s infinite; }

  @keyframes codeL1 { 0%, 2% { opacity: 0; } 5%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }
  @keyframes codeL2 { 0%, 5% { opacity: 0; } 9%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }
  @keyframes codeL3 { 0%, 9% { opacity: 0; } 13%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }
  @keyframes codeL4 { 0%, 13% { opacity: 0; } 17%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }
  @keyframes codeL5 { 0%, 17% { opacity: 0; } 21%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }
  @keyframes codeL6 { 0%, 21% { opacity: 0; } 25%, 96% { opacity: 1; } 99%, 100% { opacity: 0; } }

  /* Pointer & Visualizer animations for Problem 1 (Two Sum) */
  .p1-ptr { animation: p1PtrMove 12s infinite; }
  @keyframes p1PtrMove {
    0%, 30% { transform: translateX(0); }
    40%, 92% { transform: translateX(64px); }
    96%, 100% { transform: translateX(0); }
  }

  .p1-hashmap-fill { animation: p1MapAnim 12s infinite; }
  @keyframes p1MapAnim {
    0%, 34% { opacity: 0; transform: translateY(6px); }
    40%, 92% { opacity: 1; transform: translateY(0); }
    96%, 100% { opacity: 0; }
  }

  .p1-match-pulse { animation: p1MatchAnim 12s infinite; }
  @keyframes p1MatchAnim {
    0%, 46% { opacity: 0; transform: scale(0.98); }
    52%, 92% { opacity: 1; transform: scale(1); }
    96%, 100% { opacity: 0; }
  }

  /* Problem 2 (Binary Search) */
  .p2-shrink-l { animation: p2ShrinkL 12s infinite; }
  @keyframes p2ShrinkL {
    0%, 36% { opacity: 0.15; }
    42%, 92% { opacity: 0.85; }
    96%, 100% { opacity: 0.15; }
  }

  .p2-mid-ptr { animation: p2MidMove 12s infinite; }
  @keyframes p2MidMove {
    0%, 32% { transform: translateX(0); }
    42%, 92% { transform: translateX(96px); }
    96%, 100% { transform: translateX(0); }
  }

  /* Problem 3 (Valid Parentheses / Stack) */
  .p3-push1 { animation: p3Drop1 12s infinite; }
  .p3-push2 { animation: p3Drop2 12s infinite; }
  .p3-push3 { animation: p3Drop3 12s infinite; }
  .p3-popAll { animation: p3PopAnim 12s infinite; }

  @keyframes p3Drop1 {
    0%, 24% { opacity: 0; transform: translateY(-16px); }
    29%, 66% { opacity: 1; transform: translateY(0); }
    70%, 100% { opacity: 0; }
  }
  @keyframes p3Drop2 {
    0%, 30% { opacity: 0; transform: translateY(-16px); }
    36%, 60% { opacity: 1; transform: translateY(0); }
    65%, 100% { opacity: 0; }
  }
  @keyframes p3Drop3 {
    0%, 37% { opacity: 0; transform: translateY(-16px); }
    43%, 54% { opacity: 1; transform: translateY(0); }
    58%, 100% { opacity: 0; }
  }
  @keyframes p3PopAnim {
    0%, 64% { opacity: 0; }
    69%, 92% { opacity: 1; }
    96%, 100% { opacity: 0; }
  }

  /* Problem 4 (Sliding Window) */
  .p4-win-slide { animation: p4Slide 12s infinite; }
  @keyframes p4Slide {
    0%, 28% { transform: translateX(0); width: 88px; }
    38%, 56% { transform: translateX(46px); width: 130px; }
    66%, 92% { transform: translateX(92px); width: 134px; }
    96%, 100% { transform: translateX(0); width: 88px; }
  }

  /* Test Case Step Animations */
  .test-step-1 { animation: tStep1 12s infinite; }
  .test-step-2 { animation: tStep2 12s infinite; }
  .test-step-3 { animation: tStep3 12s infinite; }
  .test-verdict { animation: tVerdict 12s infinite; }

  @keyframes tStep1 {
    0%, 58% { opacity: 0.25; }
    63%, 94% { opacity: 1; }
    97%, 100% { opacity: 0.25; }
  }
  @keyframes tStep2 {
    0%, 66% { opacity: 0.25; }
    71%, 94% { opacity: 1; }
    97%, 100% { opacity: 0.25; }
  }
  @keyframes tStep3 {
    0%, 74% { opacity: 0.25; }
    79%, 94% { opacity: 1; }
    97%, 100% { opacity: 0.25; }
  }
  @keyframes tVerdict {
    0%, 80% { opacity: 0; transform: scale(0.96); }
    84%, 93% { opacity: 1; transform: scale(1); }
    96%, 100% { opacity: 0; }
  }

]]></style>

<!-- Background Grid Pattern -->
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
  <path d="M24 0H0V24" fill="none" stroke="#0e1724" stroke-width="0.8"/>
</pattern>

<!-- Cyan Gradient for Highlights -->
<linearGradient id="cyanGrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#4fd8ff" stop-opacity="0.9"/>
  <stop offset="100%" stop-color="#0088cc" stop-opacity="0.7"/>
</linearGradient>

<!-- Green Gradient for Accepted Verdict -->
<linearGradient id="accGrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#3ddc97" stop-opacity="0.25"/>
  <stop offset="100%" stop-color="#3ddc97" stop-opacity="0.08"/>
</linearGradient>

<!-- Scanline Gradient -->
<linearGradient id="scanGrad" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#4fd8ff" stop-opacity="0"/>
  <stop offset="50%" stop-color="#4fd8ff" stop-opacity="0.12"/>
  <stop offset="100%" stop-color="#4fd8ff" stop-opacity="0"/>
</linearGradient>

<!-- Glow Filter -->
<filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="3" result="blur" />
  <feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
<filter id="glowGreen" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="4" result="blur" />
  <feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
</defs>

<!-- Main Outer Window Frame (1000x400) -->
<rect width="1000" height="400" rx="12" fill="#070b12"/>
<rect width="1000" height="400" rx="12" fill="url(#grid)"/>
<rect x="0.5" y="0.5" width="999" height="399" rx="12" fill="none" stroke="#1b2a3a" stroke-width="1.2"/>

<!-- Animated Subtle Scanline -->
<g class="scanline">
  <rect x="2" y="44" width="996" height="32" fill="url(#scanGrad)"/>
</g>

<!-- ============================================================== -->
<!-- TOP WINDOW CONTROL BAR (y: 0 - 42)                             -->
<!-- ============================================================== -->
<rect x="0" y="0" width="1000" height="42" rx="12" fill="#0b1118"/>
<rect x="0" y="30" width="1000" height="12" fill="#0b1118"/>
<line x1="0" y1="42" x2="1000" y2="42" stroke="#182535" stroke-width="1"/>

<!-- Window Indicator Dots -->
<circle cx="24" cy="21" r="5" fill="#f43f5e" opacity="0.8"/>
<circle cx="40" cy="21" r="5" fill="#f59e0b" opacity="0.8"/>
<circle cx="56" cy="21" r="5" fill="#10b981" opacity="0.8"/>

<!-- Header Title / Live Status -->
<g transform="translate(78, 26)">
  <circle cx="0" cy="-5" r="4" fill="#3ddc97" class="blink-fast"/>
  <text class="mono" x="10" y="-1" font-size="12" font-weight="700" fill="#3ddc97" letter-spacing="1.5">LIVE DSA LAB</text>
  <text class="mono" x="122" y="-1" font-size="11" fill="#4b5c6e">|</text>
  <text class="mono" x="136" y="-1" font-size="11" font-weight="600" fill="#4fd8ff">ALGORITHM EXECUTION ENGINE</text>
  <text class="mono" x="375" y="-1" font-size="11" fill="#3a4b5d">•</text>
  <text class="mono" x="390" y="-1" font-size="11" fill="#7d92a6">JAVA 21</text>
</g>

<!-- Header Right: Raushan Kumar Identity Badge -->
<g transform="translate(980, 26)">
  <text class="mono" x="0" y="-1" text-anchor="end" font-size="11" font-weight="700" fill="#e6edf3" letter-spacing="1">RAUSHAN KUMAR <tspan fill="#4fd8ff">//</tspan> <tspan fill="#3ddc97">AUTO-SOLVER</tspan></text>
</g>

<!-- ============================================================== -->
<!-- STATIC PANEL FRAMES & LABELS                                    -->
<!-- ============================================================== -->

<!-- Left Panel Frame (Problem Specs) -->
<rect x="14" y="50" width="280" height="338" rx="8" fill="#0a0f16" stroke="#162332" stroke-width="1"/>
<rect x="14" y="50" width="280" height="28" rx="8" fill="#0e1722"/>
<rect x="14" y="70" width="280" height="8" fill="#0e1722"/>
<line x1="14" y1="78" x2="294" y2="78" stroke="#162332" stroke-width="1"/>
<text class="mono" x="26" y="68" font-size="11" font-weight="700" fill="#70879d" letter-spacing="1.2">// PROBLEM SPEC</text>

<!-- Right-Top Panel Frame (Java Code Editor) -->
<rect x="304" y="50" width="682" height="162" rx="8" fill="#060a10" stroke="#162332" stroke-width="1"/>
<rect x="304" y="50" width="682" height="28" rx="8" fill="#0e1622"/>
<rect x="304" y="70" width="682" height="8" fill="#0e1622"/>
<line x1="304" y1="78" x2="986" y2="78" stroke="#162332" stroke-width="1"/>

<!-- Editor Tab -->
<rect x="314" y="55" width="132" height="23" rx="4" fill="#060a10" stroke="#223447" stroke-width="1"/>
<path d="M324 64h8v7c0 2-2 3-4 3s-4-1-4-3v-7zm0 2h8" fill="none" stroke="#f59e0b" stroke-width="1.2"/>
<text class="mono" x="338" y="71" font-size="11" font-weight="600" fill="#e6edf3">Solution.java</text>
<circle cx="434" cy="67" r="3" fill="#3ddc97"/>

<!-- Editor Header Right -->
<text class="mono" x="972" y="69" text-anchor="end" font-size="10" fill="#50667d">OPENJDK 21 <tspan fill="#3ddc97">● JIT COMPILED</tspan></text>

<!-- Right-Bottom Panel Frame (Live Trace & Test Bench) -->
<rect x="304" y="220" width="682" height="168" rx="8" fill="#090e15" stroke="#162332" stroke-width="1"/>
<rect x="304" y="220" width="682" height="28" rx="8" fill="#0e1622"/>
<rect x="304" y="240" width="682" height="8" fill="#0e1622"/>
<line x1="304" y1="248" x2="986" y2="248" stroke="#162332" stroke-width="1"/>

<text class="mono" x="318" y="238" font-size="11" font-weight="700" fill="#70879d" letter-spacing="1.2">// ALGORITHM TRACE &amp; TEST BENCH</text>
<text class="mono" x="780" y="238" font-size="10" fill="#50667d">STATUS: <tspan fill="#3ddc97">OPTIMIZED O(1)/O(n)</tspan></text>

<!-- ============================================================== -->
<!-- SCENE 1: TWO SUM (HashMap)                                      -->
<!-- ============================================================== -->
<g class="scene scene-1">
  <!-- Left Panel Info -->
  <g transform="translate(26, 98)">
    <rect x="0" y="0" width="46" height="18" rx="3" fill="#1e293b"/>
    <text class="mono" x="23" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8">#001</text>
    <rect x="52" y="0" width="52" height="18" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
    <text class="mono" x="78" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#3ddc97">EASY</text>
    
    <text class="sans" x="0" y="38" font-size="19" font-weight="800" fill="#ffffff" letter-spacing="0.3">Two Sum</text>
    
    <!-- Concept Badge -->
    <rect x="0" y="48" width="118" height="20" rx="4" fill="#082f49" stroke="#0ea5e9" stroke-width="0.8"/>
    <text class="mono" x="59" y="62" text-anchor="middle" font-size="10" font-weight="700" fill="#38bdf8">CONCEPT: HASHMAP</text>

    <!-- Problem Specs -->
    <text class="mono" x="0" y="86" font-size="10" fill="#64748b">INPUT:</text>
    <text class="mono" x="0" y="100" font-size="11" font-weight="600" fill="#4fd8ff">nums = [2, 7, 11, 15]</text>
    <text class="mono" x="0" y="116" font-size="11" font-weight="600" fill="#f59e0b">target = 9</text>

    <text class="mono" x="0" y="140" font-size="10" fill="#64748b">GOAL:</text>
    <text class="mono" x="0" y="154" font-size="10.5" fill="#94a3b8">Find [i, j] such that</text>
    <text class="mono" x="0" y="168" font-size="10.5" fill="#e2e8f0">nums[i] + nums[j] == 9</text>

    <!-- Complexity Snapshot -->
    <line x1="0" y1="184" x2="256" y2="184" stroke="#1e293b"/>
    <text class="mono" x="0" y="202" font-size="10" fill="#64748b">TIME COMPLEXITY:</text>
    <text class="mono" x="256" y="202" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(n) One-Pass</text>
    <text class="mono" x="0" y="222" font-size="10" fill="#64748b">SPACE COMPLEXITY:</text>
    <text class="mono" x="256" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(n) Hash Table</text>

    <!-- Verified Badge -->
    <rect x="0" y="238" width="256" height="30" rx="5" fill="#0f1f18" stroke="#166534" stroke-width="1"/>
    <text class="mono" x="128" y="257" text-anchor="middle" font-size="11" font-weight="700" fill="#3ddc97">ALGORITHM SOLVED ✓</text>
  </g>

  <!-- Right-Top: Java Code Editor -->
  <g transform="translate(318, 96)">
    <text class="mono" x="0" y="14" font-size="11" fill="#334155">1</text>
    <text class="mono" x="0" y="30" font-size="11" fill="#334155">2</text>
    <text class="mono" x="0" y="46" font-size="11" fill="#334155">3</text>
    <text class="mono" x="0" y="62" font-size="11" fill="#334155">4</text>
    <text class="mono" x="0" y="78" font-size="11" fill="#334155">5</text>
    <text class="mono" x="0" y="94" font-size="11" fill="#334155">6</text>

    <g class="code-l1">
      <text class="mono" x="24" y="14" font-size="11">
        <tspan fill="#c084fc">public int</tspan><tspan fill="#e2e8f0">[]</tspan> <tspan fill="#67e8f9">twoSum</tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">int</tspan><tspan fill="#e2e8f0">[]</tspan> <tspan fill="#e2e8f0">nums, </tspan><tspan fill="#c084fc">int</tspan> <tspan fill="#e2e8f0">target</tspan><tspan fill="#94a3b8">) {</tspan>
      </text>
    </g>
    <g class="code-l2">
      <text class="mono" x="24" y="30" font-size="11">
        <tspan fill="#e2e8f0">    Map&lt;Integer, Integer&gt; map = </tspan><tspan fill="#c084fc">new</tspan> <tspan fill="#67e8f9">HashMap</tspan><tspan fill="#e2e8f0">&lt;&gt;();</tspan>
      </text>
    </g>
    <g class="code-l3">
      <text class="mono" x="24" y="46" font-size="11">
        <tspan fill="#c084fc">    for </tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">int</tspan> <tspan fill="#e2e8f0">i = 0; i &lt; nums.length; i++) {</tspan>
      </text>
    </g>
    <g class="code-l4">
      <text class="mono" x="24" y="62" font-size="11">
        <tspan fill="#c084fc">        int </tspan><tspan fill="#e2e8f0">comp = target - nums[i];</tspan>
        <tspan fill="#52525b"> // lookup in O(1)</tspan>
      </text>
    </g>
    <g class="code-l5">
      <text class="mono" x="24" y="78" font-size="11">
        <tspan fill="#c084fc">        if </tspan><tspan fill="#94a3b8">(map.containsKey(comp)) </tspan><tspan fill="#c084fc">return new int</tspan><tspan fill="#e2e8f0">[]{ map.get(comp), i };</tspan>
      </text>
    </g>
    <g class="code-l6">
      <text class="mono" x="24" y="94" font-size="11">
        <tspan fill="#e2e8f0">        map.put(nums[i], i); </tspan><tspan fill="#94a3b8">}</tspan> <tspan fill="#c084fc">return new int</tspan><tspan fill="#e2e8f0">[0]; }</tspan>
        <tspan fill="#3ddc97" class="blink-cursor">▮</tspan>
      </text>
    </g>
  </g>

  <!-- Right-Bottom: Visual Algorithm Execution -->
  <g transform="translate(318, 260)">
    <text class="mono" x="0" y="10" font-size="10" fill="#71717a">ARRAY: nums[]</text>
    
    <!-- Index 0: 2 -->
    <rect x="0" y="18" width="54" height="34" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text class="mono" x="27" y="39" text-anchor="middle" font-size="13" font-weight="700" fill="#38bdf8">2</text>
    <text class="mono" x="27" y="62" text-anchor="middle" font-size="9" fill="#64748b">i=0</text>

    <!-- Index 1: 7 -->
    <rect x="64" y="18" width="54" height="34" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text class="mono" x="91" y="39" text-anchor="middle" font-size="13" font-weight="700" fill="#38bdf8">7</text>
    <text class="mono" x="91" y="62" text-anchor="middle" font-size="9" fill="#64748b">i=1</text>

    <!-- Index 2: 11 -->
    <rect x="128" y="18" width="54" height="34" rx="4" fill="#090e17" stroke="#1e293b" stroke-width="1"/>
    <text class="mono" x="155" y="39" text-anchor="middle" font-size="13" font-weight="700" fill="#475569">11</text>
    <text class="mono" x="155" y="62" text-anchor="middle" font-size="9" fill="#475569">i=2</text>

    <!-- Index 3: 15 -->
    <rect x="192" y="18" width="54" height="34" rx="4" fill="#090e17" stroke="#1e293b" stroke-width="1"/>
    <text class="mono" x="219" y="39" text-anchor="middle" font-size="13" font-weight="700" fill="#475569">15</text>
    <text class="mono" x="219" y="62" text-anchor="middle" font-size="9" fill="#475569">i=3</text>

    <!-- Moving Current Pointer -->
    <g class="p1-ptr">
      <path d="M27 12 l-4 -6 h8 z" fill="#f59e0b"/>
      <text class="mono" x="27" y="3" text-anchor="middle" font-size="9" font-weight="700" fill="#f59e0b">CURR</text>
    </g>

    <!-- Live HashMap Representation -->
    <g transform="translate(262, 0)">
      <text class="mono" x="0" y="10" font-size="10" fill="#71717a">HASHMAP: { key: index }</text>
      <rect x="0" y="18" width="138" height="52" rx="4" fill="#0c1320" stroke="#1e3a5f" stroke-width="1"/>
      <g class="p1-hashmap-fill">
        <text class="mono" x="10" y="36" font-size="11" fill="#94a3b8">2 → <tspan fill="#4fd8ff" font-weight="700">0</tspan></text>
        <text class="mono" x="10" y="52" font-size="10" fill="#3ddc97">comp = 9-7 = 2 ✓</text>
      </g>
    </g>

    <!-- Complement Match Connector -->
    <g class="p1-match-pulse" transform="translate(0, 72)">
      <rect x="0" y="0" width="400" height="26" rx="4" fill="#062e24" stroke="#10b981" stroke-width="1"/>
      <text class="mono" x="200" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#3ddc97">MATCH FOUND: complement 2 in Map → return [0, 1]</text>
    </g>

    <!-- Right Side: Test Cases & Acceptance -->
    <g transform="translate(424, 0)">
      <line x1="0" y1="0" x2="0" y2="104" stroke="#182535" stroke-width="1"/>
      
      <g transform="translate(16, 0)">
        <text class="mono" x="0" y="10" font-size="10" fill="#71717a">TEST SUITE (3/3)</text>
        
        <g class="test-step-1">
          <text class="mono" x="0" y="28" font-size="10" fill="#94a3b8">TEST 01: [2,7,11,15], 9</text>
          <text class="mono" x="190" y="28" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-2">
          <text class="mono" x="0" y="44" font-size="10" fill="#94a3b8">TEST 02: [3,2,4], 6</text>
          <text class="mono" x="190" y="44" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-3">
          <text class="mono" x="0" y="60" font-size="10" fill="#94a3b8">TEST 03: [3,3], 6</text>
          <text class="mono" x="190" y="60" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>

        <!-- Big Accepted Badge -->
        <g class="test-verdict accepted-glow" transform="translate(0, 68)">
          <rect x="0" y="0" width="200" height="34" rx="5" fill="url(#accGrad)" stroke="#3ddc97" stroke-width="1.2"/>
          <text class="mono" x="100" y="16" text-anchor="middle" font-size="12" font-weight="800" fill="#3ddc97">✓ ACCEPTED</text>
          <text class="mono" x="100" y="29" text-anchor="middle" font-size="9" fill="#a7f3d0">1ms • Beats 99.2% (Java)</text>
        </g>
      </g>
    </g>
  </g>
</g>

<!-- ============================================================== -->
<!-- SCENE 2: BINARY SEARCH                                          -->
<!-- ============================================================== -->
<g class="scene scene-2">
  <!-- Left Panel Info -->
  <g transform="translate(26, 98)">
    <rect x="0" y="0" width="46" height="18" rx="3" fill="#1e293b"/>
    <text class="mono" x="23" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8">#704</text>
    <rect x="52" y="0" width="52" height="18" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
    <text class="mono" x="78" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#3ddc97">EASY</text>
    
    <text class="sans" x="0" y="38" font-size="19" font-weight="800" fill="#ffffff" letter-spacing="0.3">Binary Search</text>
    
    <!-- Concept Badge -->
    <rect x="0" y="48" width="158" height="20" rx="4" fill="#082f49" stroke="#0ea5e9" stroke-width="0.8"/>
    <text class="mono" x="79" y="62" text-anchor="middle" font-size="10" font-weight="700" fill="#38bdf8">CONCEPT: DIVIDE &amp; CONQUER</text>

    <!-- Problem Specs -->
    <text class="mono" x="0" y="86" font-size="10" fill="#64748b">INPUT:</text>
    <text class="mono" x="0" y="100" font-size="11" font-weight="600" fill="#4fd8ff">nums = [-1, 0, 3, 5, 9, 12]</text>
    <text class="mono" x="0" y="116" font-size="11" font-weight="600" fill="#f59e0b">target = 9</text>

    <text class="mono" x="0" y="140" font-size="10" fill="#64748b">GOAL:</text>
    <text class="mono" x="0" y="154" font-size="10.5" fill="#94a3b8">Search target in sorted</text>
    <text class="mono" x="0" y="168" font-size="10.5" fill="#e2e8f0">array in O(log n) time</text>

    <!-- Complexity Snapshot -->
    <line x1="0" y1="184" x2="256" y2="184" stroke="#1e293b"/>
    <text class="mono" x="0" y="202" font-size="10" fill="#64748b">TIME COMPLEXITY:</text>
    <text class="mono" x="256" y="202" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(log n) Logarithmic</text>
    <text class="mono" x="0" y="222" font-size="10" fill="#64748b">SPACE COMPLEXITY:</text>
    <text class="mono" x="256" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(1) Iterative</text>

    <!-- Verified Badge -->
    <rect x="0" y="238" width="256" height="30" rx="5" fill="#0f1f18" stroke="#166534" stroke-width="1"/>
    <text class="mono" x="128" y="257" text-anchor="middle" font-size="11" font-weight="700" fill="#3ddc97">ALGORITHM SOLVED ✓</text>
  </g>

  <!-- Right-Top: Java Code Editor -->
  <g transform="translate(318, 96)">
    <text class="mono" x="0" y="14" font-size="11" fill="#334155">1</text>
    <text class="mono" x="0" y="30" font-size="11" fill="#334155">2</text>
    <text class="mono" x="0" y="46" font-size="11" fill="#334155">3</text>
    <text class="mono" x="0" y="62" font-size="11" fill="#334155">4</text>
    <text class="mono" x="0" y="78" font-size="11" fill="#334155">5</text>
    <text class="mono" x="0" y="94" font-size="11" fill="#334155">6</text>

    <g class="code-l1">
      <text class="mono" x="24" y="14" font-size="11">
        <tspan fill="#c084fc">public int</tspan> <tspan fill="#67e8f9">search</tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">int</tspan><tspan fill="#e2e8f0">[]</tspan> <tspan fill="#e2e8f0">nums, </tspan><tspan fill="#c084fc">int</tspan> <tspan fill="#e2e8f0">target</tspan><tspan fill="#94a3b8">) {</tspan>
      </text>
    </g>
    <g class="code-l2">
      <text class="mono" x="24" y="30" font-size="11">
        <tspan fill="#e2e8f0">    int left = 0, right = nums.length - 1;</tspan>
      </text>
    </g>
    <g class="code-l3">
      <text class="mono" x="24" y="46" font-size="11">
        <tspan fill="#c084fc">    while </tspan><tspan fill="#94a3b8">(left &lt;= right) {</tspan>
        <tspan fill="#c084fc"> int </tspan><tspan fill="#e2e8f0">mid = left + (right - left) / 2;</tspan>
      </text>
    </g>
    <g class="code-l4">
      <text class="mono" x="24" y="62" font-size="11">
        <tspan fill="#c084fc">        if </tspan><tspan fill="#94a3b8">(nums[mid] == target) </tspan><tspan fill="#c084fc">return </tspan><tspan fill="#e2e8f0">mid;</tspan>
        <tspan fill="#52525b"> // match found</tspan>
      </text>
    </g>
    <g class="code-l5">
      <text class="mono" x="24" y="78" font-size="11">
        <tspan fill="#c084fc">        else if </tspan><tspan fill="#94a3b8">(nums[mid] &lt; target) </tspan><tspan fill="#e2e8f0">left = mid + 1;</tspan>
      </text>
    </g>
    <g class="code-l6">
      <text class="mono" x="24" y="94" font-size="11">
        <tspan fill="#c084fc">        else </tspan><tspan fill="#e2e8f0">right = mid - 1; </tspan><tspan fill="#94a3b8">}</tspan> <tspan fill="#c084fc">return </tspan><tspan fill="#e2e8f0">-1; }</tspan>
        <tspan fill="#3ddc97" class="blink-cursor">▮</tspan>
      </text>
    </g>
  </g>

  <!-- Right-Bottom: Visual Binary Search Trace -->
  <g transform="translate(318, 260)">
    <text class="mono" x="0" y="10" font-size="10" fill="#71717a">SORTED ARRAY: SEARCH SPACE SHRINKING</text>
    
    <!-- Discarded left half animation -->
    <g class="p2-shrink-l">
      <!-- 0: -1 -->
      <rect x="0" y="18" width="44" height="34" rx="4" fill="#18181b" stroke="#3f3f46" stroke-width="0.8"/>
      <text class="mono" x="22" y="39" text-anchor="middle" font-size="12" fill="#71717a">-1</text>
      <!-- 1: 0 -->
      <rect x="48" y="18" width="44" height="34" rx="4" fill="#18181b" stroke="#3f3f46" stroke-width="0.8"/>
      <text class="mono" x="70" y="39" text-anchor="middle" font-size="12" fill="#71717a">0</text>
      <!-- 2: 3 -->
      <rect x="96" y="18" width="44" height="34" rx="4" fill="#18181b" stroke="#3f3f46" stroke-width="0.8"/>
      <text class="mono" x="118" y="39" text-anchor="middle" font-size="12" fill="#71717a">3</text>
    </g>

    <!-- Active range: 5, 9, 12 -->
    <!-- 3: 5 -->
    <rect x="144" y="18" width="44" height="34" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text class="mono" x="166" y="39" text-anchor="middle" font-size="12" font-weight="700" fill="#38bdf8">5</text>
    <text class="mono" x="166" y="62" text-anchor="middle" font-size="9" fill="#64748b">i=3</text>

    <!-- 4: 9 (TARGET) -->
    <rect x="192" y="18" width="44" height="34" rx="4" fill="#062e24" stroke="#10b981" stroke-width="1.5"/>
    <text class="mono" x="214" y="39" text-anchor="middle" font-size="13" font-weight="800" fill="#3ddc97">9</text>
    <text class="mono" x="214" y="62" text-anchor="middle" font-size="9" font-weight="700" fill="#3ddc97">i=4 ✓</text>

    <!-- 5: 12 -->
    <rect x="240" y="18" width="44" height="34" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text class="mono" x="262" y="39" text-anchor="middle" font-size="12" font-weight="700" fill="#38bdf8">12</text>
    <text class="mono" x="262" y="62" text-anchor="middle" font-size="9" fill="#64748b">i=5</text>

    <!-- Mid pointer moving -->
    <g class="p2-mid-ptr">
      <path d="M118 12 l-4 -6 h8 z" fill="#f59e0b"/>
      <text class="mono" x="118" y="3" text-anchor="middle" font-size="9" font-weight="700" fill="#f59e0b">MID</text>
    </g>

    <!-- Search convergence explanation -->
    <g transform="translate(0, 72)">
      <rect x="0" y="0" width="400" height="26" rx="4" fill="#082f49" stroke="#0ea5e9" stroke-width="1"/>
      <text class="mono" x="200" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#38bdf8">nums[mid] == 9 → FOUND AT INDEX 4 in 2 STEPS</text>
    </g>

    <!-- Right Side: Test Cases & Acceptance -->
    <g transform="translate(424, 0)">
      <line x1="0" y1="0" x2="0" y2="104" stroke="#182535" stroke-width="1"/>
      
      <g transform="translate(16, 0)">
        <text class="mono" x="0" y="10" font-size="10" fill="#71717a">TEST SUITE (3/3)</text>
        
        <g class="test-step-1">
          <text class="mono" x="0" y="28" font-size="10" fill="#94a3b8">TEST 01: [-1..12], 9</text>
          <text class="mono" x="190" y="28" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-2">
          <text class="mono" x="0" y="44" font-size="10" fill="#94a3b8">TEST 02: [-1..12], 2</text>
          <text class="mono" x="190" y="44" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-3">
          <text class="mono" x="0" y="60" font-size="10" fill="#94a3b8">TEST 03: [5], 5</text>
          <text class="mono" x="190" y="60" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>

        <!-- Big Accepted Badge -->
        <g class="test-verdict accepted-glow" transform="translate(0, 68)">
          <rect x="0" y="0" width="200" height="34" rx="5" fill="url(#accGrad)" stroke="#3ddc97" stroke-width="1.2"/>
          <text class="mono" x="100" y="16" text-anchor="middle" font-size="12" font-weight="800" fill="#3ddc97">✓ ACCEPTED</text>
          <text class="mono" x="100" y="29" text-anchor="middle" font-size="9" fill="#a7f3d0">0ms • Beats 100% (Java)</text>
        </g>
      </g>
    </g>
  </g>
</g>

<!-- ============================================================== -->
<!-- SCENE 3: VALID PARENTHESES (Stack)                             -->
<!-- ============================================================== -->
<g class="scene scene-3">
  <!-- Left Panel Info -->
  <g transform="translate(26, 98)">
    <rect x="0" y="0" width="46" height="18" rx="3" fill="#1e293b"/>
    <text class="mono" x="23" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8">#020</text>
    <rect x="52" y="0" width="52" height="18" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
    <text class="mono" x="78" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#3ddc97">EASY</text>
    
    <text class="sans" x="0" y="38" font-size="19" font-weight="800" fill="#ffffff" letter-spacing="0.3">Valid Parens</text>
    
    <!-- Concept Badge -->
    <rect x="0" y="48" width="138" height="20" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.8"/>
    <text class="mono" x="69" y="62" text-anchor="middle" font-size="10" font-weight="700" fill="#c084fc">CONCEPT: STACK (LIFO)</text>

    <!-- Problem Specs -->
    <text class="mono" x="0" y="86" font-size="10" fill="#64748b">INPUT:</text>
    <text class="mono" x="0" y="100" font-size="11" font-weight="600" fill="#4fd8ff">s = "({[]})"</text>
    <text class="mono" x="0" y="116" font-size="11" font-weight="600" fill="#f59e0b">order: nested brackets</text>

    <text class="mono" x="0" y="140" font-size="10" fill="#64748b">GOAL:</text>
    <text class="mono" x="0" y="154" font-size="10.5" fill="#94a3b8">Ensure brackets are closed</text>
    <text class="mono" x="0" y="168" font-size="10.5" fill="#e2e8f0">in correct symmetric order</text>

    <!-- Complexity Snapshot -->
    <line x1="0" y1="184" x2="256" y2="184" stroke="#1e293b"/>
    <text class="mono" x="0" y="202" font-size="10" fill="#64748b">TIME COMPLEXITY:</text>
    <text class="mono" x="256" y="202" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(n) Linear Scan</text>
    <text class="mono" x="0" y="222" font-size="10" fill="#64748b">SPACE COMPLEXITY:</text>
    <text class="mono" x="256" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(n) Deque Stack</text>

    <!-- Verified Badge -->
    <rect x="0" y="238" width="256" height="30" rx="5" fill="#0f1f18" stroke="#166534" stroke-width="1"/>
    <text class="mono" x="128" y="257" text-anchor="middle" font-size="11" font-weight="700" fill="#3ddc97">ALGORITHM SOLVED ✓</text>
  </g>

  <!-- Right-Top: Java Code Editor -->
  <g transform="translate(318, 96)">
    <text class="mono" x="0" y="14" font-size="11" fill="#334155">1</text>
    <text class="mono" x="0" y="30" font-size="11" fill="#334155">2</text>
    <text class="mono" x="0" y="46" font-size="11" fill="#334155">3</text>
    <text class="mono" x="0" y="62" font-size="11" fill="#334155">4</text>
    <text class="mono" x="0" y="78" font-size="11" fill="#334155">5</text>
    <text class="mono" x="0" y="94" font-size="11" fill="#334155">6</text>

    <g class="code-l1">
      <text class="mono" x="24" y="14" font-size="11">
        <tspan fill="#c084fc">public boolean</tspan> <tspan fill="#67e8f9">isValid</tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">String</tspan> <tspan fill="#e2e8f0">s</tspan><tspan fill="#94a3b8">) {</tspan>
      </text>
    </g>
    <g class="code-l2">
      <text class="mono" x="24" y="30" font-size="11">
        <tspan fill="#e2e8f0">    Deque&lt;Character&gt; stack = </tspan><tspan fill="#c084fc">new</tspan> <tspan fill="#67e8f9">ArrayDeque</tspan><tspan fill="#e2e8f0">&lt;&gt;();</tspan>
      </text>
    </g>
    <g class="code-l3">
      <text class="mono" x="24" y="46" font-size="11">
        <tspan fill="#c084fc">    for </tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">char</tspan> <tspan fill="#e2e8f0">c : s.toCharArray()) {</tspan>
      </text>
    </g>
    <g class="code-l4">
      <text class="mono" x="24" y="62" font-size="11">
        <tspan fill="#c084fc">        if </tspan><tspan fill="#94a3b8">(c == '(') stack.push(')');</tspan>
        <tspan fill="#c084fc"> else if </tspan><tspan fill="#94a3b8">(c == '{') stack.push('}');</tspan>
      </text>
    </g>
    <g class="code-l5">
      <text class="mono" x="24" y="78" font-size="11">
        <tspan fill="#c084fc">        else if </tspan><tspan fill="#94a3b8">(c == '[') stack.push(']');</tspan>
      </text>
    </g>
    <g class="code-l6">
      <text class="mono" x="24" y="94" font-size="11">
        <tspan fill="#c084fc">        else if </tspan><tspan fill="#94a3b8">(stack.isEmpty() || stack.pop() != c) </tspan><tspan fill="#c084fc">return false;</tspan> <tspan fill="#94a3b8">}</tspan>
        <tspan fill="#3ddc97" class="blink-cursor">▮</tspan>
      </text>
    </g>
  </g>

  <!-- Right-Bottom: Visual Stack Engine Trace -->
  <g transform="translate(318, 260)">
    <text class="mono" x="0" y="10" font-size="10" fill="#71717a">INPUT TOKENS &amp; STACK BUCKET</text>

    <!-- Token stream -->
    <g transform="translate(0, 20)">
      <text class="mono" x="0" y="14" font-size="11" fill="#64748b">TOKENS:</text>
      <rect x="60" y="0" width="22" height="20" rx="3" fill="#1e1b4b"/>
      <text class="mono" x="71" y="14" text-anchor="middle" font-size="11" fill="#c084fc">(</text>
      <rect x="86" y="0" width="22" height="20" rx="3" fill="#1e1b4b"/>
      <text class="mono" x="97" y="14" text-anchor="middle" font-size="11" fill="#c084fc">{</text>
      <rect x="112" y="0" width="22" height="20" rx="3" fill="#1e1b4b"/>
      <text class="mono" x="123" y="14" text-anchor="middle" font-size="11" fill="#c084fc">[</text>
      <text class="mono" x="140" y="14" font-size="11" fill="#3ddc97">→</text>
      <rect x="156" y="0" width="22" height="20" rx="3" fill="#064e3b"/>
      <text class="mono" x="167" y="14" text-anchor="middle" font-size="11" fill="#3ddc97">]</text>
      <rect x="182" y="0" width="22" height="20" rx="3" fill="#064e3b"/>
      <text class="mono" x="193" y="14" text-anchor="middle" font-size="11" fill="#3ddc97">}</text>
      <rect x="208" y="0" width="22" height="20" rx="3" fill="#064e3b"/>
      <text class="mono" x="219" y="14" text-anchor="middle" font-size="11" fill="#3ddc97">)</text>
    </g>

    <!-- Vertical Stack Container (U-shape) -->
    <g transform="translate(280, 8)">
      <path d="M0 0 v54 h64 v-54" fill="none" stroke="#6366f1" stroke-width="1.5"/>
      <text class="mono" x="32" y="68" text-anchor="middle" font-size="9" fill="#818cf8">STACK (LIFO)</text>
      
      <!-- Elements inside stack -->
      <!-- Bottom: ) -->
      <g class="p3-push1" transform="translate(6, 36)">
        <rect x="0" y="0" width="52" height="15" rx="3" fill="#1e1b4b" stroke="#818cf8" stroke-width="0.8"/>
        <text class="mono" x="26" y="12" text-anchor="middle" font-size="10" font-weight="700" fill="#c084fc">')'</text>
      </g>
      <!-- Middle: } -->
      <g class="p3-push2" transform="translate(6, 19)">
        <rect x="0" y="0" width="52" height="15" rx="3" fill="#1e1b4b" stroke="#818cf8" stroke-width="0.8"/>
        <text class="mono" x="26" y="12" text-anchor="middle" font-size="10" font-weight="700" fill="#c084fc">'}'</text>
      </g>
      <!-- Top: ] -->
      <g class="p3-push3" transform="translate(6, 2)">
        <rect x="0" y="0" width="52" height="15" rx="3" fill="#1e1b4b" stroke="#818cf8" stroke-width="0.8"/>
        <text class="mono" x="26" y="12" text-anchor="middle" font-size="10" font-weight="700" fill="#c084fc">']'</text>
      </g>
    </g>

    <!-- Stack Verified State Message -->
    <g class="p3-popAll" transform="translate(0, 68)">
      <rect x="0" y="0" width="260" height="26" rx="4" fill="#062e24" stroke="#10b981" stroke-width="1"/>
      <text class="mono" x="130" y="17" text-anchor="middle" font-size="10.5" font-weight="700" fill="#3ddc97">POPPED ALL MATCHES → STACK EMPTY ✓</text>
    </g>

    <!-- Right Side: Test Cases & Acceptance -->
    <g transform="translate(424, 0)">
      <line x1="0" y1="0" x2="0" y2="104" stroke="#182535" stroke-width="1"/>
      
      <g transform="translate(16, 0)">
        <text class="mono" x="0" y="10" font-size="10" fill="#71717a">TEST SUITE (3/3)</text>
        
        <g class="test-step-1">
          <text class="mono" x="0" y="28" font-size="10" fill="#94a3b8">TEST 01: "()[]{}"</text>
          <text class="mono" x="190" y="28" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-2">
          <text class="mono" x="0" y="44" font-size="10" fill="#94a3b8">TEST 02: "({[]})"</text>
          <text class="mono" x="190" y="44" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-3">
          <text class="mono" x="0" y="60" font-size="10" fill="#94a3b8">TEST 03: "(]"</text>
          <text class="mono" x="190" y="60" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>

        <!-- Big Accepted Badge -->
        <g class="test-verdict accepted-glow" transform="translate(0, 68)">
          <rect x="0" y="0" width="200" height="34" rx="5" fill="url(#accGrad)" stroke="#3ddc97" stroke-width="1.2"/>
          <text class="mono" x="100" y="16" text-anchor="middle" font-size="12" font-weight="800" fill="#3ddc97">✓ ACCEPTED</text>
          <text class="mono" x="100" y="29" text-anchor="middle" font-size="9" fill="#a7f3d0">1ms • Beats 98.7% (Java)</text>
        </g>
      </g>
    </g>
  </g>
</g>

<!-- ============================================================== -->
<!-- SCENE 4: LONGEST SUBSTRING (Sliding Window)                    -->
<!-- ============================================================== -->
<g class="scene scene-4">
  <!-- Left Panel Info -->
  <g transform="translate(26, 98)">
    <rect x="0" y="0" width="46" height="18" rx="3" fill="#1e293b"/>
    <text class="mono" x="23" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8">#003</text>
    <rect x="52" y="0" width="60" height="18" rx="3" fill="#451a03" stroke="#f59e0b" stroke-width="0.8"/>
    <text class="mono" x="82" y="13" text-anchor="middle" font-size="10" font-weight="700" fill="#fbbf24">MEDIUM</text>
    
    <text class="sans" x="0" y="38" font-size="18" font-weight="800" fill="#ffffff" letter-spacing="0.2">Longest Substring</text>
    
    <!-- Concept Badge -->
    <rect x="0" y="48" width="168" height="20" rx="4" fill="#082f49" stroke="#0ea5e9" stroke-width="0.8"/>
    <text class="mono" x="84" y="62" text-anchor="middle" font-size="10" font-weight="700" fill="#38bdf8">CONCEPT: SLIDING WINDOW</text>

    <!-- Problem Specs -->
    <text class="mono" x="0" y="86" font-size="10" fill="#64748b">INPUT:</text>
    <text class="mono" x="0" y="100" font-size="11" font-weight="600" fill="#4fd8ff">s = "pwwkew"</text>
    <text class="mono" x="0" y="116" font-size="11" font-weight="600" fill="#f59e0b">constraint: non-repeating</text>

    <text class="mono" x="0" y="140" font-size="10" fill="#64748b">GOAL:</text>
    <text class="mono" x="0" y="154" font-size="10.5" fill="#94a3b8">Find maximum length of</text>
    <text class="mono" x="0" y="168" font-size="10.5" fill="#e2e8f0">contiguous substring</text>

    <!-- Complexity Snapshot -->
    <line x1="0" y1="184" x2="256" y2="184" stroke="#1e293b"/>
    <text class="mono" x="0" y="202" font-size="10" fill="#64748b">TIME COMPLEXITY:</text>
    <text class="mono" x="256" y="202" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(n) Two Pointers</text>
    <text class="mono" x="0" y="222" font-size="10" fill="#64748b">SPACE COMPLEXITY:</text>
    <text class="mono" x="256" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#3ddc97">O(min(m, n)) Set</text>

    <!-- Verified Badge -->
    <rect x="0" y="238" width="256" height="30" rx="5" fill="#0f1f18" stroke="#166534" stroke-width="1"/>
    <text class="mono" x="128" y="257" text-anchor="middle" font-size="11" font-weight="700" fill="#3ddc97">ALGORITHM SOLVED ✓</text>
  </g>

  <!-- Right-Top: Java Code Editor -->
  <g transform="translate(318, 96)">
    <text class="mono" x="0" y="14" font-size="11" fill="#334155">1</text>
    <text class="mono" x="0" y="30" font-size="11" fill="#334155">2</text>
    <text class="mono" x="0" y="46" font-size="11" fill="#334155">3</text>
    <text class="mono" x="0" y="62" font-size="11" fill="#334155">4</text>
    <text class="mono" x="0" y="78" font-size="11" fill="#334155">5</text>
    <text class="mono" x="0" y="94" font-size="11" fill="#334155">6</text>

    <g class="code-l1">
      <text class="mono" x="24" y="14" font-size="11">
        <tspan fill="#c084fc">public int</tspan> <tspan fill="#67e8f9">lengthOfLongestSubstring</tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">String</tspan> <tspan fill="#e2e8f0">s</tspan><tspan fill="#94a3b8">) {</tspan>
      </text>
    </g>
    <g class="code-l2">
      <text class="mono" x="24" y="30" font-size="11">
        <tspan fill="#c084fc">    int</tspan><tspan fill="#e2e8f0">[] last = </tspan><tspan fill="#c084fc">new int</tspan><tspan fill="#e2e8f0">[128]; Arrays.fill(last, -1);</tspan>
      </text>
    </g>
    <g class="code-l3">
      <text class="mono" x="24" y="46" font-size="11">
        <tspan fill="#c084fc">    int </tspan><tspan fill="#e2e8f0">maxLen = 0, left = 0;</tspan>
      </text>
    </g>
    <g class="code-l4">
      <text class="mono" x="24" y="62" font-size="11">
        <tspan fill="#c084fc">    for </tspan><tspan fill="#94a3b8">(</tspan><tspan fill="#c084fc">int</tspan> <tspan fill="#e2e8f0">right = 0; right &lt; s.length(); right++) {</tspan>
      </text>
    </g>
    <g class="code-l5">
      <text class="mono" x="24" y="78" font-size="11">
        <tspan fill="#c084fc">        char </tspan><tspan fill="#e2e8f0">c = s.charAt(right);</tspan>
        <tspan fill="#c084fc"> if </tspan><tspan fill="#94a3b8">(last[c] &gt;= left) left = last[c] + 1;</tspan>
      </text>
    </g>
    <g class="code-l6">
      <text class="mono" x="24" y="94" font-size="11">
        <tspan fill="#e2e8f0">        last[c] = right; maxLen = Math.max(maxLen, right - left + 1); </tspan><tspan fill="#94a3b8">}</tspan>
        <tspan fill="#3ddc97" class="blink-cursor">▮</tspan>
      </text>
    </g>
  </g>

  <!-- Right-Bottom: Visual Sliding Window Execution -->
  <g transform="translate(318, 260)">
    <text class="mono" x="0" y="10" font-size="10" fill="#71717a">STRING TOKENS &amp; ACTIVE SLIDING WINDOW</text>

    <!-- Characters: p  w  w  k  e  w -->
    <g transform="translate(0, 18)">
      <!-- p -->
      <rect x="0" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="20" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#e2e8f0">p</text>
      <!-- w -->
      <rect x="46" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="66" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#e2e8f0">w</text>
      <!-- w -->
      <rect x="92" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="112" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#e2e8f0">w</text>
      <!-- k -->
      <rect x="138" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="158" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#3ddc97">k</text>
      <!-- e -->
      <rect x="184" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="204" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#3ddc97">e</text>
      <!-- w -->
      <rect x="230" y="0" width="40" height="34" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text class="mono" x="250" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#3ddc97">w</text>

      <!-- Animated Sliding Window Overlay -->
      <rect class="p4-win-slide" x="0" y="-3" width="86" height="40" rx="5" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
    </g>

    <!-- Window Stats Badge -->
    <g transform="translate(286, 18)">
      <rect x="0" y="0" width="124" height="42" rx="4" fill="#0c1320" stroke="#1e3a5f" stroke-width="1"/>
      <text class="mono" x="10" y="18" font-size="10" fill="#94a3b8">WINDOW: <tspan fill="#3ddc97" font-weight="700">"kew"</tspan></text>
      <text class="mono" x="10" y="32" font-size="10" fill="#94a3b8">MAX LEN: <tspan fill="#f59e0b" font-weight="700">3</tspan></text>
    </g>

    <!-- Trace Message -->
    <g transform="translate(0, 72)">
      <rect x="0" y="0" width="410" height="26" rx="4" fill="#082f49" stroke="#0ea5e9" stroke-width="1"/>
      <text class="mono" x="205" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#38bdf8">NO REPEATS IN [k, e, w] → maxLen = 3 ("kew")</text>
    </g>

    <!-- Right Side: Test Cases & Acceptance -->
    <g transform="translate(424, 0)">
      <line x1="0" y1="0" x2="0" y2="104" stroke="#182535" stroke-width="1"/>
      
      <g transform="translate(16, 0)">
        <text class="mono" x="0" y="10" font-size="10" fill="#71717a">TEST SUITE (3/3)</text>
        
        <g class="test-step-1">
          <text class="mono" x="0" y="28" font-size="10" fill="#94a3b8">TEST 01: "abcabcbb"</text>
          <text class="mono" x="190" y="28" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-2">
          <text class="mono" x="0" y="44" font-size="10" fill="#94a3b8">TEST 02: "bbbbb"</text>
          <text class="mono" x="190" y="44" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>
        <g class="test-step-3">
          <text class="mono" x="0" y="60" font-size="10" fill="#94a3b8">TEST 03: "pwwkew"</text>
          <text class="mono" x="190" y="60" text-anchor="end" font-size="10" font-weight="700" fill="#3ddc97">PASS ✓</text>
        </g>

        <!-- Big Accepted Badge -->
        <g class="test-verdict accepted-glow" transform="translate(0, 68)">
          <rect x="0" y="0" width="200" height="34" rx="5" fill="url(#accGrad)" stroke="#3ddc97" stroke-width="1.2"/>
          <text class="mono" x="100" y="16" text-anchor="middle" font-size="12" font-weight="800" fill="#3ddc97">✓ ACCEPTED</text>
          <text class="mono" x="100" y="29" text-anchor="middle" font-size="9" fill="#a7f3d0">2ms • Beats 99.4% (Java)</text>
        </g>
      </g>
    </g>
  </g>
</g>

</svg>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")
    print(f"[SUCCESS] Generated hero SVG at {output_path} ({len(svg_content)} bytes)")

if __name__ == "__main__":
    generate_svg()
