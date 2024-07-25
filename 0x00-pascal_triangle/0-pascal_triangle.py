#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's
    triangle of n

    Args:
        n (integer): number of rows

    Returns:
        list: integers representing Pascal's triangle.
    """
    # if n is less or 0 return an empty list
    if n <= 0:
        return []

    else:
        # Initialize a variable called triangle with a list containing a
        # single element, [1], which represents the first row of the triangle.
        triangle = [[1]]

        for i in range(1, n):
            triangle.append([1])

            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

            triangle[i].append(1)
        return triangle
