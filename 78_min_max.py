# Q3. Write min_max(nums) that returns both the smallest and largest number.

# lo, hi = min_max([4, 1, 9, 3])
# print(lo, hi)   -> 1 9    

def min_max(nums):
    return min(nums), max(nums)

lo ,hi = min_max([4,1,9,3])
print(lo,hi)