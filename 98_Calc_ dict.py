# Make a dictionary calc with "add", "sub", "mul", "div" as lambdas.

# calc["div"](20, 4)  -> 5.0

calc=  {
    "add":lambda x, y : x + y,
    "sub":lambda x, y : x - y,
    "mul":lambda x, y : x * y,
    "div":lambda x, y : x / y
   }

result = calc["div"](20, 4)
print(result)










