''' Q13. Write increase() that uses global to add 10 to a global variable score.

 score = 0
increase(); increase()
print(score)   -> 20'''

score = 0
def increase():
    global score 
    score += 10
    return score
   
increase()
increase()
print(score)