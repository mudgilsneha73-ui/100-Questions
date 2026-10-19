'''Write greet(name, city="Jalandhar") that prints Hello <name> from <city>.
greet("Amit")            -> Hello Amit from Jalandhar
greet("Riya", "Delhi")   -> Hello Riya from Delhi'''

def greet(name, city = "Jalandhar"):
    print(F"Hello {name} From {city}")

greet("Amit")
greet("Riya","Delhi")
