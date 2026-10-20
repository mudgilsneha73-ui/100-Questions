'''Write apply_twice(func, x) that returns func(func(x)).

apply_twice(lambda x: x + 3, 10)  -> 16'''

 
def apply_twice(func ,x):
   first = func(x)
   second = func(first)
   return second
  
result = apply_twice(lambda x : x + 3 , 10)
print(result)

        
