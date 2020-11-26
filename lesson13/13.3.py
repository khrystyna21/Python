

def choose_func(nums, func1, func2):
    positive = True
    for i in nums:
        if i < 0:
            positive = False
    if positive is True:
        return func1(nums)
    else:
        return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [-1, -2, 3, -4, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

