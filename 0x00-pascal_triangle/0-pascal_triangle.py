#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """Create a function pascal_triangle: that returns a list of lists
       of integers representing the Pascal's triangle of n
    """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            lev = []
            a = 1
            for j in range(1, i + 1):
                lev.append(a)
                a = a * (i - j) // j
            result.append(lev)
    return result