'''write show(**kwargs) that prints each key and value.

show(name="Riya", age=20)
-> name = Riya
-> age = 20'''

def show(**kwargs):
   for key , value in kwargs.items():
      print(key,"=",value)

show(name="Riya" ,age=20)