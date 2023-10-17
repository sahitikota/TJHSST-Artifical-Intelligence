# Sahiti Kota
# 03/17/2022
import nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# from nltk.book import *
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import random
import re
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import movie_reviews
import pandas as pd
import random

# Chapter 2, Exercise 4
'''cfd = nltk.ConditionalFreqDist(
  (target, fileid[:4])
  for fileid in nltk.corpus.state_union.fileids()
  for w in nltk.corpus.state_union.words(fileid)
  for target in ['men', 'women', 'people']
  if w.lower().startswith(target))

cfd.plot()'''

# Chapter 2, Exercise 5
'''print(wn.synset('head.n.01').member_meronyms())
print(wn.synset('head.n.01').part_meronyms())
print(wn.synset('head.n.01').substance_meronyms())
print(wn.synset('head.n.01').member_holonyms())
print(wn.synset('head.n.01').part_holonyms())
print(wn.synset('head.n.01').substance_holonyms())'''

# Chapter 2, Exercise 7
# nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('however', lines=10)

# Chapter 2, Exercise 9
'''newsText = brown.words(categories = 'news')
romanceText = brown.words(categories = 'romance')
print("Vocabulary richness of news:x", len(set(newsText)) / len(newsText))
print("Vocabulary richness of romance:", len(set(romanceText)) / len(romanceText))
nltk.Text(newsText).similar('heart')
nltk.Text(romanceText).similar('heart')'''

# Chapter 2, Exercise 12
'''prondict = nltk.corpus.cmudict.dict()
print('Distinct words:', len(prondict))

wordPron = 0
for key in prondict:
    if len(prondict[key]) > 1:
        wordPron += 1
print('Fractions of words with more than one possible pronunciation:', wordPron / len(prondict))'''

# Chapter 2, Exercise 17
'''def find50MostFrequentWords(text):
  for w in text:
    if w.isalpha() and w.lower() not in stopwords.words('english'):
      fdist = FreqDist(w.lower() for w in text if w.isalpha() and w.lower())
  return fdist.most_common(50)'''

# Chapter 2, Exercise 18
'''def find50MostFrequentBigrams(text):
    bigram = list(nltk.bigrams(text))
    fdist = FreqDist(b for b in bigram if b[0].isalpha() and b[1].isalpha() and b[0] not in stopwords.words('english') and b[1] not in stopwords.words('english')) 
    return fdist.most_common(50)'''

# Chapter 2, Exercise 23
'''def zipfLaw(text):
    fdist = FreqDist([w.lower() for w in text if w.isalpha()])
    fdist = fdist.most_common()                                 
    rank = []
    freq = []
    n = 1                                                       
    for i in range(len(fdist)):
        freq.append(fdist[i][1])                                
        rank.append(n)
        n += 1
    plt.plot(rank, freq, 'bs')
    plt.xscale('log')                                          
    plt.title("Zipf's law")
    plt.xlabel('word rank')
    plt.ylabel('word frequency')
    plt.show()

# zipfLaw(nltk.corpus.gutenberg.words('austen-sense.txt'))

random_text = ''
for i in range(0,random.randrange(10000,1000000)):
    random_text+=random.choice("abcdefg ")
# print(random_text)
zipfLaw(random_text.split(' '))'''

# Chapter 2, Exercise 27
'''def average_polysemy(part_of_speech):
  lemmas = set (nltk.corpus.wordnet.all_lemma_names(part_of_speech))
  nr_of_synsets = 0
  for lemma in lemmas:
    nr_of_synsets += len(nltk.corpus.wordnet.synsets(lemma, pos = part_of_speech))
  return nr_of_synsets/len(lemmas)
print("Nouns:", average_polysemy('n'))
print("Verbs:", average_polysemy('v'))
print("Adjectives:", average_polysemy('a'))
print("Adverbs:", average_polysemy('r'))'''

# Chapter 3, Exercise 20
from bs4 import BeautifulSoup
from urllib import request

'''url = "https://weather.com/weather/tenday/l/Chantilly+VA?canonicalCityId=bb2ed16c053ba484e11cfaa80a6dccd1049118967edf227c2c14ac570185f315"
html = request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(html, "lxml").get_text()

print(soup[10000:11000])'''

# Chapter 3, Exercise 22
'''def unknown(url):
    text = urllib.request.urlopen(url).read()
    text = re.sub(r'/\<script(?:.|\n)*?\<\/>', '', text)
    text = re.sub(r'\<style(?:.|\n)*?\<\/style\>', '', text)
    soup = BeautifulSoup(text)
    content = soup.get_text()
    lowercased = re.findall(r'[\s\(\[\{]([a-z]+)', content)
    words = nltk.corpus.words.words()
    return set([w for w in lowercased if w not in words])

print(unknown('http://www.bbc.com/news'))'''

# Chapter 6, Exercise 4
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())
word_features = word_features[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(30)