"""Validate historical Home geometry and the concept runtime import graph. Current resource interactions are recorded separately."""
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
runtime = ROOT / 'assets/runtime-foundations'
for module in runtime.glob('*.mjs'):
    for name in re.findall(r'["\'`]\./([^"\'`]+\.mjs)["\'`]', module.read_text()):
        assert (runtime / name).exists(), (module.name, name)
print('PASS: six historical Home width records preserve original geometry and all concept runtime imports resolve. Current resource checks are recorded separately.')
