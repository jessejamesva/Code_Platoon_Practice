"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def containsDuplicate(self, nums: List[int]) -> bool:
    nums_dict = {}

    for i in nums:
        if i in nums_dict:
            return True
        
        else: 
            nums_dict[i] = 1
    return False


print(containsDuplicate([1, 2, 3, 1]) == True)
print(containsDuplicate([1, 2, 3, 4]) == False)
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)