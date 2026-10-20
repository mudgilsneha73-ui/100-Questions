'''Write make_adder(n) that returns a function adding n.

make_adder(5)(10)  -> 15'''

def make_adder(n):
    cal =  (lambda x : x + n)
    return cal

result = make_adder(5)
print(result(10))
