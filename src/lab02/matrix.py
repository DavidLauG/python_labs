import sys
import os
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import verify_matrix

#The parametres in list can be flot or int: transpose(mat:list[list [float | int]])
def transpose(mat:list[list [float | int]]) -> list[list[float | int]] | None:
    row_length = verify_matrix(mat)
    return[[mat[i][j] for i in range(len(mat))] for j in range(row_length)] #Return mat[i][j]
    
def row_sums(mat:list[list[float|int]]) -> list[float]:
    verify_matrix(mat)
    return [sum(row) for row in mat]

def col_sums(mat:list[list[float| int]]) -> list [float]:
    row_length = verify_matrix(mat)
    return [sum(mat[i][j] for i in range (len(mat))) for j in range(row_length)]

#print(transpose([[1, 2, 3]])) # [[1, 4], [2, 5], [3, 6]]
#print(row_sums([[-1, 1], [10, -10]])) # [6, 15]
print(col_sums([[1, 2, 3], [4, 5, 6]])) # [5, 7, 9]