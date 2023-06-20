"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""



def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in nums:
        second_num = target - i

        if second_num in nums:
            if i == second_num:
                if nums.count(second_num) == 1:
                    pass
                else:
                    return [i for i, x in enumerate(nums) if x == second_num]
            else:
                return [nums.index(i), nums.index(second_num)]


print(twoSum([3, 2, 4], 6) == [1,2])
print(twoSum([3, 3], 6) == [0, 1])
