import nltk
from nltk.tokenize import WhitespaceTokenizer
# nltk.download("punkt")

filename = input()
# filename = "corpus.txt"
f = open(filename, "r", encoding="utf-8")
corpus = f.read()
# print(corpus[0:2])

tkns = WhitespaceTokenizer().tokenize(corpus)
# print(tkns[0:5])

bigrams = list(nltk.bigrams(tkns))
print("Number of bigrams:", len(bigrams))

while True:
    in_ = input()
    try:
        idx = int(in_)
        print("Head:", bigrams[idx][0], "Tail:", bigrams[idx][1])
    except ValueError:
        if in_ == "exit":
            False
            break
        else:
            print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please put input a value that is not greater than the number of all bigrams.")