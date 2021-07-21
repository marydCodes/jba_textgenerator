import re

good_string = 'You learn Python 3?..'
bad_string = 'You learn Python 3?!.'
template = 'You learn Python 3\?\.\.'

# print(re.match(template, good_string)) # match obj
# print(re.match(template, bad_string)) # None