# Sahiti Kota
# 05/20/2022
import nltk
import ssl
import re
from nltk.corpus import wordnet as wn
from nltk.corpus import udhr
ssl._create_default_https_context = ssl._create_unverified_context

# Chapter 2, Exercise 26
'''cnt = 0
hypos = 0
for synset in wn.all_synsets('n'):
    if synset.hyponyms() != []:
        hypos += len(synset.hyponyms())
        cnt += 1
print(hypos / cnt)'''

# Chapter 2, Exercise 25

'''def find_language(s):
    langs = []
    for lang in udhr.fileids():
        if lang.endswith('Latin1') and s in udhr.words(lang):
            langs.append(lang)
    return langs

print(find_language('eye'))'''

# Chapter 3, Exercise 40
'''def ari(raw):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(raw)
    words = nltk.word_tokenize(raw)
    av_wordlength = sum(len(w) for w in words) / len(words)
    av_sentlength = sum(len(s) for s in sents) / len(sents)
    return (4.71 * av_wordlength) + (0.5 * av_sentlength) - 21.43

print(ari(nltk.corpus.abc.raw("rural.txt")))
print(ari(nltk.corpus.abc.raw("science.txt")))'''

# Chapter 3, Exercise 41
'''words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vowelSequences = [''.join(re.findall(r'[aeiou]', vowel)) for vowel in words]
print(sorted(vowelSequences))'''

# Chapter 7, Exercise 13

import nltk
# Tagged corpus
brown = nltk.corpus.brown

grammar = r"""
    NOUNP: {<DT>?<JJ.*>*<NN.*>+} # Noun phrase
    CLAUSE: {<VB><IN><NOUNP>}    # Verb
    """
cp = nltk.RegexpParser(grammar)

tuples = set()

for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CLAUSE':
            tuples.add((subtree[0][0],subtree[1][0], "NP"))

for t in sorted(tuples):
    print(t)