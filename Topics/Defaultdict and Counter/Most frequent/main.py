import collections

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split()

n = int(input())

most_comn = collections.Counter(text_list).most_common(n)
for i in most_comn:
    print(*i)
