from nltk.tokenize import regexp_tokenize

text = input()
num = int(input())
tkns = regexp_tokenize(text, "[A-z]+")
print(tkns[num])