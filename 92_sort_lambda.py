'''. Sort ["pear", "fig", "banana"] by length using a lambda.

-> ['fig', 'pear', 'banana']'''

word = ['pear' , 'fig', 'banana']


key = lambda word: len(word)
print(sorted(word , key = key)) 

# print(sorted(word , key =  lambda word: len(word)))   ---  both are correct



