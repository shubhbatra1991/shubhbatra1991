"""Data-integrity and animation fallback checks using synthetic test fixtures only."""
import importlib.util
from pathlib import Path
from datetime import date, timedelta
import unittest
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location('defender', Path(__file__).with_name('generate-commit-defender.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DefenderTests(unittest.TestCase):
    def setUp(self):
        self.days = [(date(2025, 1, 5)+timedelta(days=i), i % 5) for i in range(365)]
        self.html = ''.join(f'<td data-date="{d}" data-level="{level}"></td>' for d, level in self.days)

    def test_calendar_is_preserved(self):
        self.assertEqual(module.parse_calendar(self.html), self.days)
        root = ET.fromstring(module.render(self.days))
        cells = [e for e in root.iter() if e.tag.endswith('rect') and len(e) and e[0].tag.endswith('title')]
        self.assertEqual(len(cells), len(self.days))
        self.assertEqual([c.get('fill') for c in cells], [module.COLORS[level] for _, level in self.days])

    def test_bad_data_fails_closed(self):
        for html in ['', self.html+self.html, self.html.replace('data-level="4"', 'data-level="9"'), self.html.replace('<td data-date="2025-02-01" data-level="2"></td>', '')]:
            with self.subTest(html=html[:60]), self.assertRaises(ValueError):
                module.parse_calendar(html)

    def test_static_has_no_animations_or_dependencies(self):
        svg = module.render(self.days, animated=False)
        root = ET.fromstring(svg)
        self.assertFalse(any('animate' in e.tag for e in root.iter()))
        self.assertNotIn('href=', svg)
        self.assertNotIn('<script', svg)

    def test_zero_activity_has_no_invented_targets(self):
        svg = module.render([(d, 0) for d, _ in self.days])
        self.assertNotIn('class="projectile"', svg)
        self.assertNotIn('animateTransform', svg)


if __name__ == '__main__':
    unittest.main()
