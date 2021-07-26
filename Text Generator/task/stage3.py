# Stage 3 /6: make a simplified version of a Markov chain model

import nltk
from nltk.tokenize import WhitespaceTokenizer
import collections
# nltk.download("punkt")

# filename = input()
filename = "corpus.txt"
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
        frq_dict = collections.Counter(bgr_dict[head]) # dictionary-type of "tails": num_occurrences
        most_comn = frq_dict.most_common() # list of ("tails" and num_occurrences)? Same as frq_dict, but sorted desc
        for i in most_comn:
            print(f"Tail: {i[0]}\t\t\tCount: {i[1]}")