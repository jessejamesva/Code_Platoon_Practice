def maxArea(height):
    left = ()
    right = ()
    line_max_area = 0

    points_arr = [(k, v) for k, v in enumerate(height)]
    # [(0, 1), (1, 8), (2, 6), (3, 2), (4, 5), (5, 4), (6, 8), (7, 3), (8, 7)]

    points_arr.sort(key=lambda x: x[1], reverse=True)

    def compare_points(a, b):
        if a[1] < b[1]:
            horz_line = a[1]
        else:
            horz_line = b[1]

        distance = b[0] - a[0]
        test_area = horz_line * distance
        return test_area

    if points_arr[0][0] < points_arr[1][0]:
        left = points_arr[0]
        right = points_arr[1]
    else:
        left = points_arr[1]
        right = points_arr[0]

    res = compare_points(left, right)
    if line_max_area < res:
        line_max_area = res
    print(left, right)
    print(line_max_area)

    reset_left = left

    while left[0] > 0:

        left = (left[0]-1, height[left[0]-1])
        res = compare_points(left, right)
        if line_max_area < res:
            line_max_area = res
        print(f'left: {left}, MA: {line_max_area}')

    left = reset_left

    while right[0] < len(height)-1:

        right = (right[0]+1, height[right[0]+1])
        res = compare_points(left, right)
        if line_max_area < res:
            line_max_area = res
        print(f'right: {right}, MA: {line_max_area}')

    while left[0] > 0:

        left = (left[0]-1, height[left[0]-1])
        res = compare_points(left, right)
        if line_max_area < res:
            line_max_area = res
        print(f'left: {left}, MA: {line_max_area}')

    return line_max_area


# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
# print(maxArea([1, 1]) == 1)
# print(maxArea([1, 2, 3, 4]) == 4)
# print(maxArea([4, 3, 2, 1, 4]) == 16)
print(maxArea([9, 6, 14, 11, 2, 2, 4, 9, 3, 8]) == 72)
