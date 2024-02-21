#!/usr/bin/python3
""" doc """


def _find_next(current):
    """ helper func to find the next ele of the list"""
    next_element = [1]
    last_element = current[-1]
    for i in range(len(last_element)):
        if i == len(last_element)-1:
            next_element.append(1)
            return next_element
        next_element.append(last_element[i]+last_element[i+1])


def pascal_triangle(n):
    """ doc """
    res = [[1]]
    for i in range(n-1):
        res.append(_find_next(res))
    return res
