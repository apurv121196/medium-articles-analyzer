from sys import argv
from os import listdir
from gensim.models.doc2vec import Doc2Vec, TaggedDocument, LabeledSentence
from nltk.tokenize import word_tokenize
from tqdm import tqdm
query = argv[1:]

def load_data(query):
    data = []
    labels = []
    for q in tqdm(query):
        path = f'./{q}/docs/'
        files = listdir(path)
        for f in tqdm(files):
            data.append(open(path + f, 'r').read())
            labels.append(q)
    return data, labels
data, labels = load_data(query)
print('Loaded Data')
class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=word_tokenize(doc.lower()),tags=[self.labels_list[idx]])

it = LabeledLineSentence(data, labels)

model = Doc2Vec(size=400, window=7, min_count=5, workers=11,alpha=0.025, min_alpha=0.025, iter=200) # use fixed learning rate
model.build_vocab(it)
for epoch in tqdm(range(model.iter)):
    model.train(it, epochs=model.iter, total_examples=model.corpus_count)
# model.train(it, epochs=model.iter, total_examples=model.corpus_count)


model.save('doc2vec.model')