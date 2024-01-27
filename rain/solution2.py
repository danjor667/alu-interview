#!/usr/bin/python3


def trap(height: list) -> int:
    """
    >>> nums = [4,2,0,3,2,5]
    >>> print(trap(nums))
    9
    """
    i = 0
    j = len(height) - 1
    max_left = height[i]
    max_right = height[j]
    max_area = 0
    while i <= j:
        if max_left <= max_right:
            if max_left <= height[i]:
                max_left = height[i]
            max_area += max_left - height[i]
            i += 1
        else:
            if max_right <= height[j]:
                max_right = height[j]
            max_area += max_right - height[j]
            j -= 1
    return max_area


"""
time complexity O(n)
space complexity O(1)
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
