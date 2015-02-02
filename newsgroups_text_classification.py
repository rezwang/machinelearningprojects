#The 20 Newsgroups data set is a collection of approximately 20,000 newsgroup documents, partitioned (nearly) evenly across 20 different newsgroups. To the best of my knowledge, it was originally collected by Ken Lang, probably for his Newsweeder: Learning to filter netnews paper, though he does not explicitly mention this collection. The 20 newsgroups collection has become a popular data set for experiments in text applications of machine learning techniques, such as text classification and text clustering.

#sklearn.datasets.fetch_20newsgroups function is a data fetching / caching functions that downloads the data archive from the original 20 newsgroups website, extracts the archive contents in the ~/scikit_learn_data/20news_home folder and calls the sklearn.datasets.load_file on either the training or testing set folder, or both of them
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train')

from pprint import pprint
pprint(list(newsgroups_train.target_names))

#The real data lies in the filenames and target attributes. The target attribute is the integer index of the category
#newsgroups_train.filenames.shape
#newsgroups_train.target.shape
#newsgroups_train.target[:10]


#load only a sub-selection of the categories by passing the list of the categories to load to the fetch_20newsgroups function:

cats = ['alt.atheism', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
list(newsgroups_train.target_names)
['alt.atheism', 'sci.space']
newsgroups_train.filenames.shape
newsgroups_train.target.shape
newsgroups_train.target[:10]