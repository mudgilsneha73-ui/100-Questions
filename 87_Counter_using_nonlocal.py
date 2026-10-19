'''Write make_counter() using nonlocal, so that each call of the returned function gives 1, 2, 3.

c = make_counter()
print(c(), c(), c())   -> 1 2 3'''


def make_counter():
    count = 0 

    def multi_counter():
        nonlocal count
        count += 1
        return(count)
    return multi_counter