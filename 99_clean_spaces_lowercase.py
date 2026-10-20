'''Write clean(words) that removes extra spaces and makes each word lowercase, using map.

clean(["  Hello ", "WORLD  "])  -> ['hello', 'world']'''

def clean(words):
  
    c = list(map(lambda x : (x.strip().lower()), words))
    return c

words = clean(["  Hello ", "WORLD  "])
print(words)