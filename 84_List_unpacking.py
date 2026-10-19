''' Call add(a, b) using a list [3, 4] with * unpacking.

-> 7'''

def add(a,b):

    total = a + b
    return total

lst = [3,4]

result = add(*lst)
print(result)