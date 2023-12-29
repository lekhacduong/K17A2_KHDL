nums = [2,6,7,9]
def has_Lucky_numbers(nums):
    for i in nums:
        if i % 7 == 0:
            a=True
            break
        else:
            a=False
    return a
        
print(has_Lucky_numbers(nums))