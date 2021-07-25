# Stage 3 /6: make a simplified version of a Markov chain model

import nltk
from nltk.tokenize import WhitespaceTokenizer
import collections
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
print("Number of bigrams:", len(bigrams))

# dictionary of bigrams
bgr_dict = collections.defaultdict(list)
# print(bgr_dict)
for trn in bigrams:
    bgr_dict[trn[0]].append(trn[1])
# print(bgr_dict)

head = '0'
while head != 'exit':
    head = input()
    if head == 'exit':
        break
    elif head not in bgr_dict:
        print(f"Head: {head}")
        print("Key Error. The requested word is not in the model. Please input another word.")
    else:
        print(f"Head: {head}")
        frq_dict = collections.Counter(bgr_dict[head])
        most_comn = frq_dict.most_common()
        for i in most_comn:
            print(f"Tail: {i[0]}\tCount: {i[1]}")