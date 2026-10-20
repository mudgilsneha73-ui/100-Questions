'''Write compose(f, g) that returns a function computing f(g(x)).

add1 = lambda x: x + 1
double = lambda x: x * 2
compose(add1, double)(5)  -> 11'''

def compose(f, g):
    return lambda x: f(g(x))


add1 = lambda x: x + 1
double = lambda x: x * 2

result = compose(add1, double)(5)
print(result)

