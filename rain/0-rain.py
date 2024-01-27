#!/usr/bin/python3


def trap(height: list) -> int:
    """
    >>> nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    >>> print(trap(nums))
    6
    """

    if not height or height == []:
        return 0
    if len(height) < 3:
        return 0

    max_area = 0
    for i in range(len(height)):
        max_left = max(height[0:i+1])
        max_right = max(height[i:])
        area = min(max_left, max_right) - height[i]
        if area < 0:
            area == 0
        max_area += area
    return max_area


"""
time complexity O(n^2)
space complexity O(1)
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
