# Write average(*nums) that returns 0 if no numbers are given.

# average(2, 4, 6)  -> 4.0
# average()         -> 0

def average(*nums):
    if len(nums) == 0:
        return 0
    else:
      average = sum(nums) / len(nums)
      return average

result = average(2,4,6)
print(result)

print(
average())

