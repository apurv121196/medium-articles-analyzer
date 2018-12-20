from sys import argv
from os import listdir
from gensim.models.doc2vec import Doc2Vec, TaggedDocument, LabeledSentence
from nltk.tokenize import word_tokenize
from tqdm import tqdm
query = argv[1:]
model = Doc2Vec.load('doc2vec.model')

ans = model.most_similar(query)

print(ans)