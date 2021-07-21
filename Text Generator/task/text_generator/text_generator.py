from nltk.tokenize import WhitespaceTokenizer
# nltk.download("punkt")

filename = input()
# filename = "corpus.txt"
f = open(filename, "r", encoding="utf-8")
corpus = f.read()
# print(corpus[0:2])

tkns = WhitespaceTokenizer().tokenize(corpus)
# tkns = regexp_tokenize(corpus, "[0-9A-z'\-!]+")
# print(tkns[0:5])

# Corpus statistics
n_all = len(tkns)
n_unq = len(set(tkns))
print("Corpus statistics")
print("All tokens:", n_all)
print("Unique tokens:", n_unq)

while True:
    in_ = input()
    try:
        idx = int(in_)
        print(tkns[idx])
    except ValueError:
        if in_ == "exit":
            False
            break
        else:
            print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please put input an integer that is in the range of the corpus.")