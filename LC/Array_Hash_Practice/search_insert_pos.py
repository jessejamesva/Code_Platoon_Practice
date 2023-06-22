"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 
 """
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # step 1: set initial range to include entire list
    low = 0
    high = len(nums)-1

    # step 2 & 6: loop as long as low stays lower    
    while low <= high:

        # step 3: find the middle
        mid = ( low + high ) // 2

        # step 4 & 5: compare mid index to target, adj range
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        # target equals mid, return target index
        else:
            return mid
    
    # step 7: return previous low if loop stops
    return low