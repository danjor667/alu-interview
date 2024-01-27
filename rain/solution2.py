#!/usr/bin/python3


def rain(walls: list) -> int:
    """
    >>> nums = [4,2,0,3,2,5]
    >>> print(rain(nums))
    9
    """
    i = 0
    j = len(walls) - 1
    max_left = walls[i]
    max_right = walls[j]
    max_area = 0
    while i <= j:
        if max_left <= max_right:
            if max_left <= walls[i]:
                max_left = walls[i]
            max_area += max_left - walls[i]
            i += 1
        else:
            if max_right <= walls[j]:
                max_right = walls[j]
            max_area += max_right - walls[j]
            j -= 1
    return max_area


"""
time complexity O(n)
space complexity O(1)
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
