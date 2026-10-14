"""Regenerate the local README hero. Python standard library only."""

from pathlib import Path
from html import escape

DESTINATION = Path(__file__).resolve().parents[1] / "assets" / "hero"


def hero(mobile=False, animated=True):
    w, h = (600, 438) if mobile else (1200, 422)
    left = 34 if mobile else 58
    name_y = 158 if mobile else 177
    name_size = 49 if mobile else 76
    roles = [
        "Frontend-Led Full Stack Engineer",
        "Building AI-Powered Products",
        "Engineering Interactive Experiences",
        "Turning Ideas Into Software",
    ]
    role_y = 210 if mobile else 234
    role_size = 23 if mobile else 28
    # Each phrase is visible for 5 seconds. Two cycles, then the first phrase
    # remains visible. Static files contain no animation or CSS at all.
    motion = """
    <style>
      .r0 { animation: first 20s 2; }
      .r1 { opacity: 0; animation: second 20s 2; }
      .r2 { opacity: 0; animation: third 20s 2; }
      .r3 { opacity: 0; animation: fourth 20s 2; }
      @keyframes first { 0%,22% {opacity:1} 25%,97% {opacity:0} 100% {opacity:1} }
      @keyframes second { 0%,24% {opacity:0} 27%,47% {opacity:1} 50%,100% {opacity:0} }
      @keyframes third { 0%,49% {opacity:0} 52%,72% {opacity:1} 75%,100% {opacity:0} }
      @keyframes fourth { 0%,74% {opacity:0} 77%,94% {opacity:1} 97%,100% {opacity:0} }
      @media (prefers-reduced-motion: reduce) {
        .r0 { animation:none; opacity:1 }
        .r1,.r2,.r3 { animation:none; opacity:0 }
      }
    </style>""" if animated else ""
    labels = "".join(
        f'<text class="r{i}" x="{left}" y="{role_y}" opacity="{1 if i == 0 else 0}">{escape(role)}</text>'
        for i, role in enumerate(roles if animated else roles[:1])
    )
    # The diagram is decorative; all professional information is real SVG text.
    diagram = "" if mobile else """
    <g fill="none" stroke="#244750" stroke-width="1.5">
      <path d="M907 125 L1020 190 L907 255 L794 190 Z"/>
      <path d="M907 125 V255 M794 190 H1020 M851 157 L964 222 M964 157 L851 222"/>
      <path d="M794 190 L755 212 V284 H907 V255 M1020 190 L1060 166 V109" stroke-dasharray="3 7"/>
      <path d="M851 157 L907 125 L964 157" stroke="#5eead4" stroke-width="2"/>
    </g>
    <g fill="#0d1d27" stroke="#31565f">
      <rect x="879" y="106" width="56" height="38" rx="9"/>
      <rect x="766" y="171" width="56" height="38" rx="9"/>
      <rect x="992" y="171" width="56" height="38" rx="9"/>
      <rect x="879" y="236" width="56" height="38" rx="9"/>
    </g>
    <g fill="#9cb9c6" font-family="Consolas, monospace" font-size="12" text-anchor="middle">
      <text x="907" y="130">UI</text><text x="794" y="195">API</text>
      <text x="1020" y="195">AI</text><text x="907" y="260">UX</text>
    </g>
    <circle cx="907" cy="190" r="10" fill="#5eead4"/>
    <circle cx="907" cy="190" r="22" fill="none" stroke="#5eead4" stroke-opacity=".2"/>
    <text x="907" y="314" fill="#7e9ba8" font-family="Consolas, monospace" font-size="11" letter-spacing="2" text-anchor="middle">SYSTEMS / WITH A HUMAN INTERFACE</text>
    """
    bottom = 320 if mobile else 325
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="title desc">
  <title id="title">Saurabh Batra — Frontend-Led Full Stack Engineer</title>
  <desc id="desc">Building AI-powered products, engineering interactive experiences, and turning ideas into software.</desc>
  <defs>
    <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0c1722"/><stop offset="1" stop-color="#091017"/></linearGradient>
    <linearGradient id="edge"><stop stop-color="#5eead4"/><stop offset="1" stop-color="#4f8ac9" stop-opacity=".25"/></linearGradient>
    <radialGradient id="glow"><stop stop-color="#134e4a" stop-opacity=".3"/><stop offset="1" stop-color="#134e4a" stop-opacity="0"/></radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#7cb0ba" stroke-opacity=".035"/></pattern>
  </defs>
  {motion}
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="url(#bg)" stroke="#28404d"/>
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="17" fill="url(#grid)"/>
  <ellipse cx="{w-160}" cy="190" rx="290" ry="205" fill="url(#glow)"/>
  <path d="M22 49 H{w-22}" stroke="#21313e"/>
  <g fill="#4b6371"><circle cx="{left}" cy="26" r="4"/><circle cx="{left+16}" cy="26" r="4"/><circle cx="{left+32}" cy="26" r="4"/></g>
  <text x="{left+62}" y="30" fill="#93adba" font-family="Consolas, monospace" font-size="11" letter-spacing="1">saurabh@github ~ / portfolio</text>
  <text x="{left}" y="{100 if mobile else 112}" fill="#5eead4" font-family="Consolas, monospace" font-size="13" letter-spacing="3">ENGINEERING / INTERFACES / EXPERIENCES</text>
  <text x="{left-3}" y="{name_y}" fill="#eff8fb" font-family="Segoe UI, Arial, sans-serif" font-size="{name_size}" font-weight="700" letter-spacing="-2">SAURABH BATRA</text>
  <g fill="#5eead4" font-family="Segoe UI, Arial, sans-serif" font-size="{role_size}" font-weight="500">{labels}</g>
  <text x="{left}" y="{260 if mobile else 276}" fill="#9ab1bf" font-family="Consolas, monospace" font-size="{16 if mobile else 16}">Frontend craft. Full-stack thinking.</text>
  {diagram}
  <path d="M{left} {bottom} H{w-left}" stroke="url(#edge)"/>
  <text x="{left}" y="{bottom+34}" fill="#70909e" font-family="Consolas, monospace" font-size="12">$</text>
  <text x="{left+20}" y="{bottom+34}" fill="#c4d6df" font-family="Consolas, monospace" font-size="{15 if mobile else 14}">build thoughtful software</text>
  <rect x="{left+(240 if mobile else 225)}" y="{bottom+21}" width="7" height="16" fill="#5eead4" opacity=".7"/>
  <text x="{left}" y="{bottom+66}" fill="#8aa5b4" font-family="Consolas, monospace" font-size="{13 if mobile else 12}" letter-spacing="1">REACT · TYPESCRIPT · FULL STACK · AI · UNITY</text>
</svg>
'''


if __name__ == "__main__":
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for mobile in (False, True):
        for animated in (True, False):
            name = "terminal" + ("-mobile" if mobile else "") + ("" if animated else "-static")
            path = DESTINATION / f"{name}.svg"
            path.write_text(hero(mobile, animated), encoding="utf-8")
            print(path.relative_to(DESTINATION.parents[1]))
