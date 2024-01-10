#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_result = []
    for row in matrix:
        squared_result.append([x**2 for x in row])
    return squared_result
