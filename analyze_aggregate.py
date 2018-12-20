import sys
import json

query = sys.argv[1]
agg_path = f'./{query}/aggregate.json'
agg = json.loads(open(agg_path, 'r').read())
sorted_agg = sorted(agg.items(), key = lambda x: x[1]['relevance'] * (1 if 'count' not in x else x[1]['count']), reverse = True)
for i in range(20):
    print(sorted_agg[i])