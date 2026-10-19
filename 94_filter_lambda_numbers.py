'''Use filter and a lambda to keep only numbers greater than 10.

[5, 12, 8, 20, 3]  -> [12, 20]'''

numbers = [5, 12, 8, 20, 3] 

result = filter( lambda x : x > 10, numbers)

print(list(result))
