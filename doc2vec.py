import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import sys
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

articles = sys.argv[1:]
docs = []
index_to_file = []
for art in articles:
    [docs.append(i) for i in [open(f'./{art}/docs/{j}').read() for j in os.listdir(f'./{art}/docs/')] ]
    [index_to_file.append(j) for j in os.listdir(f'./{art}/docs/')]
    # docs.append(open('./Ethos/docs/Ethos.html').read())
# print(np.array(docs).shape)
# papers = ['Scoop', 'Ethos']

features = tfidf.fit_transform(docs).toarray()
# ls = np.array([0]*len(os.listdir(f'./{articles[0]}/docs/')) + [1]*len(os.listdir(f'./{articles[1]}/docs/')))
labels = np.array([])
for i, j in enumerate(articles):
    labels = np.concatenate((labels, [i]*len(os.listdir(f'./{j}/docs/'))))
    # [labels.append(m) for m in [i]*len(os.listdir(f'./{j}/docs/'))]
# print(ls, len(ls), type(ls))
# print(labels, len(labels), type(labels))
N = 10
for category, category_id in [(articles[i], i) for i in range(len(articles))]:
    # print(sum(labels == [category_id]*len(labels)))
    # print(labels == category_id)
    features_chi2 = chi2(features, labels == category_id)
    # features_chi2 = chi2(features, [False]*len(labels))
    print(features_chi2)
    indices = np.argsort(features_chi2[0])
    feature_names = np.array(tfidf.get_feature_names())[indices]
    unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
    bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
    print("# '{}':".format(category))
    print("  . Most correlated unigrams:\n       . {}".format('\n       . '.join(unigrams[-N:])))
    print("  . Most correlated bigrams:\n       . {}".format('\n       . '.join(bigrams[-N:])))

# print(np.array(tfidf.get_feature_names()))

SAMPLE_SIZE = int(len(features) * 0.3)
np.random.seed(0)
# indices = np.random.choice(range(len(features)), size=SAMPLE_SIZE, replace=False)
indices = list(range(len(features)))
print(features[(labels == 2)].shape)
projected_features = TSNE(n_components=2, random_state=0).fit_transform(features[indices])
colors = ['pink', 'green', 'midnightblue', 'orange', 'darkgrey']
for category, category_id in [(articles[i], i) for i in range(len(articles))]:
    points = projected_features[(labels[indices] == category_id)]
    mark_points = [i for i, j in enumerate(points[:0] < -75) if j == True] & [i for i, j in enumerate(points[:1] < 0) if j == True]
    indices = [i for i, x in enumerate(mark_points) if x == True]
    for i in index_to_file[indices]:
        print(i) 
    plt.scatter(points[:, 0], points[:, 1], s=30, c=colors[category_id], label=category)
plt.title("  tf-idf feature vector for each article, projected on 2 dimensions.",
          fontdict=dict(fontsize=15))
plt.legend()
plt.show()