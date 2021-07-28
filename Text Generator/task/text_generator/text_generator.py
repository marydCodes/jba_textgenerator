import random
from collections import defaultdict, Counter

file = input()
f = open(file, "r", encoding="utf-8")
words = [' '.join(x.split()) for x in f]
words = ' '.join(words).split()
bigrams = list(zip(words, words[1:]))
freq = defaultdict(Counter)
for head, tail in bigrams:
    freq[head][tail] += 1


def start(corpus):
    if corpus[0].isupper() and corpus[-1] not in ['!', '.', '?']:
        return corpus
    return start(random.choice(words))


def check(sentence):
    return False if len(sentence.split()) >= 5 and sentence.split()[-1][-1] in ['!', '.', '?'] else True


result = []
for _ in range(10):
    word = start(random.choice(words))
    texts = word
    while generating := check(texts):
        data = [num[1] for num in freq[word].items()]
        next_word = [*freq[word].keys()]
        text = random.choices(next_word, data)[0]
        texts += ' ' + text
        word = text
    result.append(texts)

print(*result, sep='\n')