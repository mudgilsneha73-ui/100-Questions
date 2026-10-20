'''Use reduce to find the product of [2, 3, 4].

-> 24'''

from functools import reduce 

numbers = [2,3,4]

product = reduce(lambda a, b: a * b, numbers)

print(product)
