"""Render public GitHub calendar levels as original SVG artwork; no API token needed."""
import argparse
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
import urllib.request

SOURCE = 'https://github.com/users/shubhbatra1991/contributions'
COLORS = ['#172c3b', '#115d43', '#168357', '#29b96e', '#7ae99b']


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and 'data-date' in a and 'data-level' in a:
            day, level = date.fromisoformat(a['data-date']), int(a['data-level'])
            if level not in range(5) or day in self.days:
                raise ValueError('Unexpected or duplicate contribution data')
            self.days[day] = level


def parse_calendar(html):
    parser = Calendar()
    parser.feed(html)
    days = sorted(parser.days.items())
    if not 350 <= len(days) <= 371:
        raise ValueError('Incomplete public calendar; refusing to generate synthetic data')
    if any(b[0] - a[0] != timedelta(days=1) for a, b in zip(days, days[1:])):
        raise ValueError('Non-contiguous calendar')
    return days


def animate(attribute, values, times):
    return (f'<animate attributeName="{attribute}" values="{values}" '
            f'keyTimes="{times}" dur="20s" repeatCount="indefinite"/>')


def render(days, animated=True):
    start = days[0][0] - timedelta(days=(days[0][0].weekday()+1) % 7)
    def position(day):
        offset = (day-start).days
        return 50 + (offset//7)*14, 64 + (offset % 7)*14

    active = [day for day, level in days if level]
    targets = [active[(i*(len(active)-1))//3] for i in range(4)] if len(active) >= 4 else active
    cells, effects = [], []
    ship_x = [position(day)[0]+5 for day in targets]
    for day, level in days:
        x, y = position(day)
        cells.append(f'<rect x="{x}" y="{y}" width="10" height="10" rx="1" fill="{COLORS[level]}"><title>{day}: GitHub activity level {level}/4</title></rect>')
    times, positions = ['0'], [str(ship_x[-1] if ship_x else 420)]
    for i, day in enumerate(targets):
        x, y = position(day)
        base = i/len(targets)
        # Move, fire, impact, restore; every effect shares the same twenty-second clock.
        fire, hit, restore = [base+n/len(targets) for n in (.38, .6, .92)]
        times.extend([f'{fire:.4f}', f'{restore:.4f}'])
        positions.extend([str(x+5), str(x+5)])
        if animated:
            t = f'0;{fire:.4f};{hit:.4f};1'
            effects.append(f'<rect class="projectile" x="{x+3}" y="167" width="4" height="12" rx="2" fill="#a5fff0" stroke="#38d9df" stroke-width="4" stroke-opacity=".25" opacity="0">'+animate('y',f'167;167;{y+4};{y+4}',t)+animate('opacity','0;0;1;1;0;0',f'0;{fire:.4f};{fire+.005:.4f};{hit-.005:.4f};{hit:.4f};1')+'</rect>')
            effects.append(f'<rect class="impact" x="{x-1}" y="{y-1}" width="12" height="12" fill="#071422" opacity="0">'+animate('opacity','0;0;.85;0;0',f'0;{hit:.4f};{hit+.005:.4f};{restore:.4f};1')+'</rect>')
            for j, (dx, dy) in enumerate([(-12,-10),(12,-10),(-10,12),(10,12)]):
                t = f'0;{hit:.4f};{restore:.4f};1'
                effects.append(f'<rect class="particle" x="{x+4}" y="{y+4}" width="3" height="3" fill="{["#67e8d3","#bd9bff"][j%2]}" opacity="0">'+animate('x',f'{x+4};{x+4};{x+4+dx};{x+4+dx}',t)+animate('y',f'{y+4};{y+4};{y+4+dy};{y+4+dy}',t)+animate('opacity','0;0;.9;0;0',f'0;{hit:.4f};{hit+.005:.4f};{restore:.4f};1')+'</rect>')
    times.append('1'); positions.append(positions[0])
    ship_motion = ''
    if animated and targets:
        ship_motion = f'<animateTransform attributeName="transform" type="translate" values="{";".join(v+" 181" for v in positions)}" keyTimes="{";".join(times)}" dur="20s" repeatCount="indefinite"/>'
    ship = '<path d="M0-10H3V-4H7V1H12V7H3V4H-3V7H-12V1H-7V-4H-3V-10Z" fill="#67e8d3"/><path d="M-2-4H2V2H-2Z" fill="#123649"/><path d="M-2 7H2V12H-2Z" fill="#bd9bff"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="232" viewBox="0 0 860 232" role="img" aria-labelledby="title desc">
<title id="title">Commit Defender — Saurabh Batra</title>
<desc id="desc">A decorative arcade loop over GitHub's public contribution calendar, {days[0][0]} to {days[-1][0]}. Colors preserve GitHub activity levels, not invented counts. No repository details are collected. Energy shots briefly obscure selected active cells, which restore each loop.</desc>
<style>.still{{display:none}}@media(prefers-reduced-motion:reduce){{.motion{{display:none}}.still{{display:inline}}}}</style>
<rect x="1" y="1" width="858" height="230" rx="14" fill="#0b1828" stroke="#294355"/>
<g font-family="Segoe UI,Arial,sans-serif"><text x="28" y="32" fill="#75e9dc" font-size="21" font-weight="700" letter-spacing="2">COMMIT DEFENDER</text><text x="832" y="32" text-anchor="end" fill="#b4c9d8" font-size="14">PUBLIC CONTRIBUTION GRID</text></g>
<path d="M28 44H832M28 202H832" stroke="#284050"/>
{''.join(cells)}
<g class="motion">{''.join(effects)}<g class="ship" transform="translate({positions[0]} 181)">{ship}{ship_motion}</g></g>
<g class="still" transform="translate({positions[0]} 181)">{ship}</g>
<text x="28" y="221" fill="#9db7cb" font-family="Segoe UI,Arial,sans-serif" font-size="13">{days[0][0]} — {days[-1][0]} · GitHub public calendar · Decorative animation</text>
</svg>'''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Saved public calendar HTML for reproducible validation')
    parser.add_argument('--output', type=Path, default=Path('assets/games'))
    args = parser.parse_args()
    if args.input:
        html = args.input.read_text(encoding='utf-8')
    else:
        request = urllib.request.Request(SOURCE, headers={'User-Agent': 'Commit-Defender-public-calendar'})
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read().decode('utf-8')
    days = parse_calendar(html)
    args.output.mkdir(parents=True, exist_ok=True)
    for animated, suffix in [(True, ''), (False, '-static')]:
        (args.output / f'commit-defender{suffix}.svg').write_text(render(days, animated), encoding='utf-8')
    print(f'Rendered {len(days)} verified daily levels from {SOURCE}; no counts inferred.')
