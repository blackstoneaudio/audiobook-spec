import yaml
import json

src = 'draft.yml'
tgt = src.replace('.yml', '.json')

with open(tgt, 'w') as t:
    t.write(json.dumps(yaml.load(open(src)), indent=2))
