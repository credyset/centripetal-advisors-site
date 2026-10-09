"""Validate recorded browser geometry and the concept runtime import graph."""
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
qa = json.loads((ROOT / 'tools/foundations-layout-qa.json').read_text())
baseline = {entry['viewport']: entry['live'] for entry in json.loads((ROOT / 'assets/baseline/layout-comparison.json').read_text())}
assert {entry['width'] for entry in qa['home']} == set(baseline)
for entry in qa['home']:
    assert entry['h1'] == ['Strategic CFO Services'] and not entry['overflow'], entry['width']
    old = {section['name']: section for section in baseline[entry['width']]['sections']}
    assert {section['name'] for section in entry['sections']} == set(old), entry['width']
    for section in entry['sections']:
        original = old[section['name']]
        shift = entry['resource']['h'] if section['name'] in {'Why Centripetal', 'Contact'} else 0
        assert section['h'] == original['h'], (entry['width'], section['name'])
        assert abs(section['y'] - original['y'] - shift) <= 1, (entry['width'], section['name'])
    assert entry['resource']['y'] == old['Why Centripetal']['y']
expected = {8:'Foundation gaps',15:'Foundation gaps',16:'Building',23:'Building',24:'Solid',31:'Solid',32:'Investor-ready',40:'Investor-ready'}
assert {int(case['total']) for case in qa['scorecard']} == set(expected)
for case in qa['scorecard']:
    assert case['count'] == '8' and case['bands'][0].startswith(expected[int(case['total'])])
runtime = ROOT / 'assets/runtime-foundations'
for module in runtime.glob('*.mjs'):
    for name in re.findall(r'["\'`]\./([^"\'`]+\.mjs)["\'`]', module.read_text()):
        assert (runtime / name).exists(), (module.name, name)
print('PASS: six recorded Home widths preserve original geometry, eight Scorecard boundaries pass, and all concept runtime imports resolve.')
