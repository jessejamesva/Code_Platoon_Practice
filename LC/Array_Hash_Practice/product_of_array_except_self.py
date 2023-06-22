"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums):
    res = []
    c = {}
    nums_temp = [x for x in nums]

    for i in range(len(nums)):
        if nums_temp[i] in c:
            res.append(c[nums[i]])
        else:
            nums_temp[i] = 1
            temp_res = 1
            for j in nums_temp:
                temp_res *= j
            res.append(temp_res)
            c[nums[i]] = temp_res
            temp_res = 1
            nums_temp[i] = nums[i]

    return res


# print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
