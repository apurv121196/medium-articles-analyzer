import sys
import json

query = sys.argv[1]
agg_path = f'./meta-docs/{query}.json'
agg = json.loads(open(agg_path, 'r').read())
sorted_agg = sorted(agg['keywords'], key = lambda x: x['relevance'] * (1 if 'count' not in x else x['count']), reverse = True)
for i in range(30):
    print(f'{i}: {sorted_agg[i]}')