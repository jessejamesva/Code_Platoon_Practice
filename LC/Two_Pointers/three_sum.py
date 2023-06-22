"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""


def threeSum(nums):
    ##### START SERACHING IND 1, THEN USE TWO POINTERS TO CHECKS REAMING COMBOS TO THE END ####
    res = {}

    if nums[0] + nums[1] + nums[2] == 0:
        check = [nums[0], nums[1], nums[2]]
        check.sort()
        res[tuple(check)] = check    

    for i in range(len(nums)-2):
        first = nums[i]                   
        
        for rem in nums[i+1:-1]:
            last = (first + rem) * -1
            if last in nums[i+2:]:
                if last == rem and nums[i+1:].count(last) == 1:
                    pass
                else:
                    check = [first, rem, last]
                    check.sort()
                    if tuple(check) not in res:
                        res[tuple(check)] = check
            

    return res.keys()

print(threeSum([-1, 0, 1, 2, -1, -4]))

##### DID NOT WORK FOR ALL CASES, DID POOR AT SEARCHING THE MIDDLE #########
# res = []
# lft = 0
# mid = 1
# rgt = 2

# for i in range(len(nums) -3):
#     if nums[lft] + nums[mid] + nums[rgt] == 0:
#         res.append([nums[lft], nums[mid], nums[rgt]])
#     rgt += 1

# for j in range(len(nums) -3):
#     if nums[lft] + nums[mid] + nums[rgt] == 0:
#         res.append([nums[lft], nums[mid], nums[rgt]])
#     mid += 1

# for k in range(len(nums) -3):
#     if nums[lft] + nums[mid] + nums[rgt] == 0:
#         res.append([nums[lft], nums[mid], nums[rgt]])
#     lft += 1
# print(lft, mid, rgt)

# for m in range(len(nums) -3):
#     if nums[lft] + nums[mid] + nums[rgt] == 0:
#         res.append([nums[lft], nums[mid], nums[rgt]])
#     lft -= 1
#     mid -= 1
#     rgt -= 1

# return res
