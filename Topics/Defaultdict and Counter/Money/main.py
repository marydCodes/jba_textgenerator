import collections

transactions = [(38177, 34.38),
                (876, 999.99),
                (654276, 653678),
                (54366, 0.99),
                (546, 987.65),
                (876, 3456),
                (654276, 0.55),
                (38177, 876.75),
                (876, 98.7)]

# create transaction_dict
transaction_dict = collections.defaultdict(list)
for k, v in transactions:
    transaction_dict[k].append(v)

# print(transaction_dict)