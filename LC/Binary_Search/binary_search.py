def search(nums, target):
        left = 0
        right = len(nums)
        

        while left <= right and left < len(nums):
            mid = (left + right) // 2
            print(left, mid, right)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid +1
            else: right = mid - 1

        return -1