from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import os
import itertools
import pickle

query = str(sys.argv[1])
print('Query:    ', query)
try:
	os.mkdir(f'./{query}')
except FileExistsError:
	pass

try:
	os.mkdir(f'./{query}/docs')
except FileExistsError:
	pass
header = {'User-Agent':'Mozilla/5.0'}
url = f'https://medium.com/search/posts?q={query}&count=500'
path = f'./{query}/'
doc_path = path + 'docs/'

'''
https://medium.com/search/posts?q=ethereum&count=10&ignore=79956138bea3&ignore=22d1df506369&ignore=9e5dc29e33ce&ignore=dcab52905bba&ignore=8fcd5f8abcdf&ignore=88718e08124f&ignore=46dd486ceecf&ignore=9401b7188841&ignore=2b650b5f4f62
'''

# soup = BeautifulSoup(urlopen(Request(url, headers=header)), 'html.parser')
links=None
while links is None:
	try:
		links = [i.a['href'] for i in BeautifulSoup(urlopen(Request(url, headers=header)), 'html.parser').findAll('div', {'class': 'postArticle-content'})]
	except:
		pass
# print(links)
f=open(f'{path}/links-{query}.txt', 'w')
f.write('\n'.join(links))
f.close()

f=open(f'{path}/links-{query}', 'wb')
pickle.dump(links, f)
f.close()
