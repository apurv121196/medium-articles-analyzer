import os
import sys
import json
from collections import Counter
query = sys.argv[1]
metadocs_path = f'./{query}/meta-docs/'
files = sorted(os.listdir(metadocs_path), key=lambda x:int(x.split('-')[1].split('.')[0]))
aggregate = {}

for f in files:
	f=open(metadocs_path + f, 'r')
	data = json.loads(f.read())['keywords']
	print(Counter({}))
	for d in data:
		print(aggregate.get(d['text'], {'relevance': 0, 'count': 0}), d)
		aggregate[d['text']] = Counter(aggregate.get(d['text'], {'relevance': 0, 'count': 0})) + Counter({i:d[i] for i in d if i!='text'})
	f.close()
f=open(f'./{query}/aggregate.json', 'w')
f.write(json.dumps(aggregate, indent=2))
f.close()