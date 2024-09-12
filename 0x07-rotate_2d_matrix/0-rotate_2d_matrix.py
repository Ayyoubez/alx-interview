#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix in place (90 degrees clockwise)."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    n = len(matrix)
    if not all(len(row) == n for row in matrix):  # Ensure the matrix is n x n
        return

    # Perform the rotation in place
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
