#  Q10. Write area(length: float, width: float) -> float with a docstring. Print area.__doc__.

def area(length: float, width: float) -> float:
    '''Returns the Area of Rectangle '''
    return length * width

result = area(23,22)
print(result)
print(area.__doc__)