# def addOne(digits):
#     n = len(digits)
#     for i in range(n - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             break
#         digits[i] = 0
#     else:
#         digits = [1] + digits
#     result = int(''.join(map(str, digits)))
#     return result
# digits=[1,3,4]
# print(addOne(digits))


def rearrange(nums):
    n=len(nums)
    res=[0]*n
    pos_index=0
    neg_index=1
    for i in range(n):
        if nums[i]>0:
            res[pos_index]=nums[i]
            pos_index+=2
        else:
            res[neg_index]=nums[i]
            neg_index+=2    
    return res
nums=[1,4,-3,6,-2,-7]
print(rearrange(nums))        