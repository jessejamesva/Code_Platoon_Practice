def maxArea(height):
    if height == []:
        return 0

    left_idx = 0
    left = height[left_idx]
    right_idx = len(height) - 1
    right = height[right_idx]

    result = 0

    if len(height) == 2:
        return 1 * min(right, left)

    for i in range(len(height)-1):
        area = (right_idx - left_idx) * min(right, left)
        result = max(result, area)

        if left < right:
            left_idx += 1
            left = height[left_idx]
        else:
            right_idx -= 1
            right = height[right_idx]

        # print(left, right)

    return result


# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(maxArea([1, 1]) == 1)
print(maxArea([1, 2, 3, 4]) == 4)
print(maxArea([4, 3, 2, 1, 4]) == 16)
print(maxArea([9, 6, 14, 11, 2, 2, 4, 9, 3, 8]) == 72)
print(maxArea([0, 2]) == 0)
