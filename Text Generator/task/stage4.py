# Stage 4/6: Generate random text
# We suggest using the method random.choices() to select the most probable tail from the list of possible tails based on the corresponding repetition counts.
# This method is similar to random.choice() with the exception that it also considers user-specified weights during the process.

import nltk
from nltk.tokenize import WhitespaceTokenizer
import collections
import random
# nltk.download("punkt")

filename = input()
# filename = "corpus.txt"
f = open(filename, "r", encoding="utf-8")
corpus = f.read()
# print(corpus[0:2])

#tokenize corpus
tkns = WhitespaceTokenizer().tokenize(corpus)
# print(tkns[0:5])

# create list of bigrams
bigrams = list(nltk.bigrams(tkns))
# print("Number of bigrams:", len(bigrams))
# print(bigrams[0:3])

# create dictionary of bigrams aka Markov model
bgr_dict = collections.defaultdict(list) # specify source of dict will be a list (of bigrams); automatically collects
# "heads" as keys and lists "tails" as values
for tup in bigrams:
     bgr_dict[tup[0]].append(tup[1])

for i in range(10):
    chain = []
    for i in range(9):
        if i == 0:
            word = random.choice(tkns)
            chain.append(word)
        else:
            word = nxt_word

        frq_dict = collections.Counter(bgr_dict[word])
        most_comn = frq_dict.most_common()
        nxt_word = most_comn[0][0]
        chain.append(nxt_word)

    pseudo = " ".join(chain)
    print(pseudo)