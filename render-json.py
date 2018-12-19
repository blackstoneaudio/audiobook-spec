import yaml
import json

for src in ['draft.yaml', 'schema.yaml']:
    tgt = src.replace('.yaml', '.json')
    with open(tgt, 'w') as t:
        t.write(json.dumps(yaml.load(open(src)), indent=2))
