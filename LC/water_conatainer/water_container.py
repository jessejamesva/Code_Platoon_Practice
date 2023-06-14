def maxArea(height):
    max_upper_val = 0
    max_upper_pos = []
    max_lower_val = 0
    max_lower_pos = []

    middle = len(height) // 2
    lower = 0
    upper = len(height) - 1

    horz_line = 0
    distance = 0

    if len(height) == 2:
        max_lower_pos = [0, height[0]]
        max_upper_pos = [1, height[1]]

    while lower < middle:
        arr_area = height[lower] * (middle - lower)
        if arr_area > max_lower_val:
            max_lower_val = arr_area
            max_lower_pos = [lower, height[lower]]
        lower += 1

    while upper > middle:
        arr_area = height[upper] * (upper - middle)
        if arr_area > max_upper_val:
            max_upper_val = arr_area
            max_upper_pos = [upper, height[upper]]
        upper -= 1

    if max_lower_pos[1] < max_upper_pos[1]:
        horz_line = max_lower_pos[1]
    else:
        horz_line = max_upper_pos[1]

    distance = max_upper_pos[0] - max_lower_pos[0]

    return horz_line * distance


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(maxArea([1, 1]) == 1)
