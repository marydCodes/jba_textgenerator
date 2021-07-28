# Stage 6/6: Generate sentences based on trigrams

import nltk
from nltk.tokenize import WhitespaceTokenizer
import collections
import random
import re
# nltk.download("punkt")

filename = input()
# filename = "corpus.txt"
f = open(filename, "r", encoding="utf-8")
corpus = f.read()

#tokenize corpus
tkns = WhitespaceTokenizer().tokenize(corpus)

# create list of bigrams
trigrams = list(nltk.ngrams(tkns, 3))

# create dictionary of trigrams aka the Markov model
tgr_dict = collections.defaultdict(list) # specify source of dict will be a list (of trigrams); automatically collects
# "heads" as keys and lists "tails" as values
for tup in trigrams:
     tgr_dict[tup[0] + " " + tup[1]].append(tup[2])

heads = list(tgr_dict.keys())

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
# for i in range(10):
for i in range(10):
    chain = []
    # print(i)
    while True:
        if len(chain) == 0:
            # get suitable start
            start_pr = random.choice(heads)
            start_wrds = start_pr.split(" ")

            while first_word_ok(start_wrds[0]) == False:
                start_pr = random.choice(heads)
                start_wrds = start_pr.split(" ")
            chain.append(start_wrds[0])
            chain.append(start_wrds[1])
        # from the 5th word on, check most_comn[0][0] for ending punct
        elif len(chain) >= 4:
            frq_dict = collections.Counter(tgr_dict[start_pr])  # dictionary-type of "tails": num_occurrences
            most_comn = frq_dict.most_common()  # list of ("tails" and num_occurrences)? Same as frq_dict, but sorted desc
            # print(most_comn[0][0])
            if last_word_punct(most_comn[0][0]) == True:
                chain.append(most_comn[0][0])
                # print(chain, len(chain))
                break
            else:
                chain.append(most_comn[0][0])
                # print(chain, len(chain))
                start_pr = " ".join(chain[len(chain) - 2:len(chain)])
        else:
            # get next word using start_pr
            frq_dict = collections.Counter(tgr_dict[start_pr])  # dictionary-type of "tails": num_occurrences
            most_comn = frq_dict.most_common()  # list of ("tails" and num_occurrences)? Same as frq_dict, but sorted desc
            chain.append(most_comn[0][0])
            # print(chain, len(chain))
            start_pr = " ".join(chain[len(chain) - 2:len(chain)])
    print(" ".join(chain))