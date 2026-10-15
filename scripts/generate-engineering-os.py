"""Original Engineering OS artwork. Self-contained SVG; standard library only."""
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / 'assets/hero'


def render(mobile=False, animated=True):
    w, h = (600, 760) if mobile else (1200, 440)
    def anim(attribute, values, times='0;.1667;.4167;.6667;1', **extra):
        attrs = ' '.join(f'{k}="{v}"' for k, v in extra.items())
        return (f'<animate attributeName="{attribute}" values="{values}" keyTimes="{times}" dur="12s" repeatCount="indefinite" {attrs}/>' if animated else '')

    def rotate(radius, duration, reverse=False):
        motion = (f'<animateTransform attributeName="transform" type="rotate" from="{360 if reverse else 0} 900 224" to="{0 if reverse else 360} 900 224" dur="{duration}s" repeatCount="indefinite"/>' if animated else '')
        return f'<g class="moving"><circle cx="900" cy="224" r="{radius}" fill="none" stroke="#5eead4" stroke-opacity=".55" stroke-width="1.5" stroke-dasharray="38 125 18 125"/>{motion}</g>'

    nodes = [(735,169,'FRONTEND','M-11-7H11V7H-11ZM0 7V12M-6 12H6'),
             (1065,169,'BACKEND','M-10-7C-10-13 10-13 10-7V8C10 14-10 14-10 8ZM-10-7C-10-1 10-1 10-7M-10 0C-10 6 10 6 10 0'),
             (900,90,'AI','M-4-10C-14-13-15 0-10 2C-15 11-3 14-1 8V-8M4-10C14-13 15 0 10 2C15 11 3 14 1 8V-8M-10 2L-5 0M10 2L5 0'),
             (755,333,'CREATIVE','M-9-8H9L15 9Q13 14 8 8L5 5H-5L-8 8Q-13 14-15 9ZM-7-5V3M-11-1H-3M7-2H7M10 1H10'),
             (1045,333,'CLOUD','M-11 8C-20 6-16-5-9-5C-9-17 10-17 11-5C21-4 19 9 11 9H-11')]
    node_svg, connections, particles = [], [], []
    for i, (x,y,label,icon) in enumerate(nodes):
        path = f'M900 224 Q{(900+x)//2} {y if y<224 else 270} {x} {y}'
        connections.append(f'<path d="{path}"/>')
        label_y = (y+6 if label == "AI" else y-35) if y<224 else y+43
        label_x = x+46 if label == "AI" else x
        label_anchor = "start" if label == "AI" else "middle"
        node_svg.append(f'''<g><circle cx="{x}" cy="{y}" r="29" fill="#071b2a" stroke="#237380"/>
<circle class="moving" cx="{x}" cy="{y}" r="32" fill="none" stroke="#40e4d7" opacity=".35">{anim('opacity','.18;.65;.4;.6;.18',begin=f'-{i*.15}s')}</circle>
<g transform="translate({x} {y})" fill="none" stroke="#b6fff6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{icon}"/></g>
<text x="{label_x}" y="{label_y}" text-anchor="{label_anchor}" fill="#d5edf6" font-size="18" font-weight="600" letter-spacing="1">{label}</text></g>''')
        if animated:
            particles.append(f'''<g class="moving" opacity="0"><circle r="10" fill="url(#spark)"/><circle r="2.5" fill="#c1fff5"/>
<animateMotion path="{path}" dur="4s" begin="{2+i*.22}s" repeatCount="indefinite"/>
<animate attributeName="opacity" values="0;.9;.9;0" keyTimes="0;.15;.8;1" dur="4s" begin="{2+i*.22}s" repeatCount="indefinite"/></g>''')
    diagram = 'translate(-434 285) scale(.82)' if mobile else 'translate(0 0)'
    product_y = 620 if mobile else 324
    product_width = 264 if mobile else 290
    second_x = 306 if mobile else 334
    products = ''
    for x, name, line1, line2 in [(30,'DealPatch','AI-assisted B2B CRM','Human-reviewed workflows'),(second_x,'SignalOps-AI','Product intelligence','Customer signals · Funnels')]:
        products += f'''<g><rect x="{x}" y="{product_y}" width="{product_width}" height="102" rx="9" fill="#0b2130" stroke="#20505f"/>
<path d="M{x+13} {product_y+20}v15" stroke="#46e6d5" stroke-width="3"/>
<text x="{x+25}" y="{product_y+29}" fill="#e7f6fa" font-size="22" font-weight="600">{name}</text>
<text x="{x+14}" y="{product_y+53}" fill="#a8c7d8" font-size="{16 if mobile else 17}">{line1}</text>
<text x="{x+14}" y="{product_y+74}" fill="#a8c7d8" font-size="{16 if mobile else 17}">{line2}</text>
{f'<text x="{x+14}" y="{product_y+94}" fill="#a8c7d8" font-size="16">Actionable insights</text>' if name == 'SignalOps-AI' else ''}</g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">Engineering OS — Saurabh Batra, Software Engineer</title>
<desc id="desc">Full-Stack Systems · AI Applications · Cloud Engineering · Interactive Experiences. React, TypeScript, Next.js, C#/.NET, Python, Azure, AI integrations and Unity. DealPatch: AI-assisted B2B CRM and human-reviewed workflows (AI is simulated in the public demo). SignalOps-AI: Product intelligence, customer signals, funnels, and actionable insights. An animated constellation connects Frontend, Backend, AI, Cloud and Creative.</desc>
<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0c2030"/><stop offset="1" stop-color="#040e1b"/></linearGradient>
<radialGradient id="aura"><stop stop-color="#2dd4bf" stop-opacity=".25"/><stop offset="1" stop-color="#2dd4bf" stop-opacity="0"/></radialGradient>
<radialGradient id="spark"><stop stop-color="#73fff0" stop-opacity=".65"/><stop offset="1" stop-color="#73fff0" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#54b3c6" stroke-opacity=".055"/></pattern>
</defs>
<style>@media(prefers-reduced-motion:reduce){{.moving{{display:none}}}}</style>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="url(#bg)" stroke="#245264"/>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="15" fill="url(#grid)"/>
<path d="M26 48H{w-26}" stroke="#235362"/>
<path d="M20 84V66H38M{w-38} {h-20}H{w-20}V{h-38}" fill="none" stroke="#3bcbbb" opacity=".65"/>
<g font-family="Segoe UI,Arial,sans-serif">
<path d="M30 33L39 17L48 33H43L39 25L35 33Z" fill="#67e8d3"/>
<text x="62" y="33" fill="#b7f5ef" font-size="17" font-weight="600" letter-spacing="3">ENGINEERING OS</text>
<text x="{w-28}" y="32" text-anchor="end" fill="#80adbd" font-size="14" letter-spacing="2">DESIGN / BUILD / EVOLVE</text>
<text x="30" y="114" fill="#f0f7fc" font-size="{48 if mobile else 53}" font-weight="700" letter-spacing="-1.5">SAURABH <tspan fill="#62e5dc">BATRA</tspan></text>
<text x="32" y="158" fill="#e0f6fa" font-size="30">Software <tspan fill="#62e5dc">Engineer</tspan></text>
<text x="32" y="196" fill="#aecddd" font-size="21"><tspan x="32">Full-Stack Systems · AI Applications ·</tspan><tspan x="32" dy="28">Cloud Engineering · Interactive Experiences</tspan></text>
<text x="32" y="266" fill="#c0dee7" font-size="19">React · TypeScript · Next.js · C#/.NET</text>
<text x="32" y="292" fill="#a0bfce" font-size="19">Python · Azure · AI integrations · Unity</text>
<g transform="{diagram}">
<ellipse cx="900" cy="224" rx="210" ry="166" fill="url(#aura)"/>
<ellipse cx="900" cy="224" rx="192" ry="69" fill="none" stroke="#217b83" stroke-opacity=".5"/>
<ellipse cx="900" cy="224" rx="167" ry="149" fill="none" stroke="#29b5b0" stroke-opacity=".27" stroke-dasharray="2 10"/>
<g fill="none" stroke="#349eaa" stroke-width="1.4">{''.join(connections)}</g>
<g fill="none" stroke="#2b8992"><circle cx="900" cy="224" r="91" opacity=".25"/><circle cx="900" cy="224" r="77" opacity=".5"/><circle cx="900" cy="224" r="61" opacity=".6"/></g>
<circle class="moving" cx="900" cy="224" r="103" fill="url(#aura)" opacity=".4">{anim('opacity','.4;.4;.55;1;.4')}</circle>
{rotate(84,36)}{rotate(68,24,True)}
<circle cx="900" cy="224" r="48" fill="#0a2332" stroke="#54e3d4" stroke-width="1.5"/>
<circle cx="900" cy="224" r="43" fill="none" stroke="#205161"/>
<path d="M887 212L873 224L887 236M913 212L927 224L913 236M906 206L894 242" fill="none" stroke="#c3fff8" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
{''.join(node_svg)}{''.join(particles)}
</g>
<text x="32" y="{product_y-10}" fill="#69d8cc" font-size="14" letter-spacing="2">FEATURED SYSTEMS</text>
{products}
<g transform="translate({32 if mobile else 705} {739 if mobile else 414})"><text fill="#86bbc9" font-family="Consolas,monospace" font-size="14">&gt;_ engineering ideas into experiences</text><rect class="moving" x="294" y="-10" width="7" height="13" fill="#67e8d3">{anim('opacity','1;1;.15;1;.15;1','0;.6667;.75;.8333;.9167;1')}</rect></g>
</g>
</svg>'''


if __name__ == '__main__':
    for mobile in (False, True):
        for animated in (True, False):
            name = 'engineering-os' + ('-mobile' if mobile else '') + ('' if animated else '-static') + '.svg'
            (OUT / name).write_text(render(mobile, animated), encoding='utf-8')
