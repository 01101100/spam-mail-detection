import re
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from os import listdir
from os.path import isfile, join

# file = open('raw-data/part1/3-1msg1.txt', 'r')

def remove_stopwords(file_content):
	words = re.sub(r'[.!,;?"#$%&\'()*+-/@<>:0-9{}/=~\\]', ' ', file_content).split()
	# words = list(set(words) - set(stopwords.words('english')))
	words_without_stopwords = [word.lower() for word in words if word not in stopwords.words('english')]
	return words_without_stopwords

def lemmatize(words):
	lmtzr = WordNetLemmatizer()
	# lemmatized_words = [lmtzr.lemmatize(word.lower()) for word in words]
	lemmatized_words = [lmtzr.lemmatize(word, pos[0].lower()) if  pos[0].lower() in ['a','n','v'] else lmtzr.lemmatize(word) for word, pos in pos_tag(words)]
	return lemmatized_words
		

# print(lemmatize(remove_stopwords(file.read())))
# print(stopwords.words('english'))
def process(path):
	file_names = listdir(path)
	for file_name in file_names:
		file = open(path + '/' + file_name, 'r')
		print(file)

process('raw-data/train')