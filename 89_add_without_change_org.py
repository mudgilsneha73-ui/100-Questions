'''Write add_99(lst) that does NOT change the original list.

nums = [1, 2]
print(add_99(nums))  -> [1, 2, 99]
print(nums)          -> [1, 2]'''

def add99(lst):
    
    new_lst = lst.copy()
    new_lst.append(99)
    return new_lst

nums = [1,2]

print(add99(nums))
print(nums)      



