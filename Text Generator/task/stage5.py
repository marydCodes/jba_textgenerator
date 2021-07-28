# Stage 5 v1

import nltk
from nltk.tokenize import WhitespaceTokenizer
import collections
import random
import re
# nltk.download("punkt")

# filename = input()
filename = "corpus.txt"
f = open(filename, "r", encoding="utf-8")
corpus = f.read()

#tokenize corpus
tkns = WhitespaceTokenizer().tokenize(corpus)

# create list of bigrams
bigrams = list(nltk.bigrams(tkns))

# create dictionary of bigrams aka the Markov model
bgr_dict = collections.defaultdict(list) # specify source of dict will be a list (of bigrams); automatically collects
# "heads" as keys and lists "tails" as values
for tup in bigrams:
     bgr_dict[tup[0]].append(tup[1])

def first_word_ok(word):
    if word[0].isupper() and word[-1] not in ".?!":
        return True
    else:
        return False

def last_word_punct(word):
    if word[-1] in ".?!":
        return True
    else:
        return False

# create sentences
for i in range(10):
    chain = []
    while len(chain) < 10:
        word = random.choice(tkns)
        if len(chain) == 0:
            while first_word_ok(word) == False:
                word = random.choice(tkns)
            chain.append(word)
        elif len(chain) == 9:
            while last_word_punct(word) == False:
                word = random.choice(tkns)
            chain.append(word)
            break
        elif len(chain) >= 4: # should be checking 5th word and on...
            if last_word_punct(word) == True:
                chain.append(word)
                break

        frq_dict = collections.Counter(bgr_dict[word])  # dictionary-type of "tails": num_occurrences
        most_comn = frq_dict.most_common()  # list of ("tails" and num_occurrences)? Same as frq_dict, but sorted desc
        nxt_word = most_comn[0][0]  # word in first item of most_comn list
        chain.append(nxt_word)

    pseudo = " ".join(chain)
    print(pseudo)