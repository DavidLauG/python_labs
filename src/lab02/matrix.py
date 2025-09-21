def transpose(mat:list[list [float | int]]) -> list[list[float | int]] | None:
    if not mat:
        return None
    row_length = len (mat[0])

    if any(len(row)!=row_length for row in mat):
        raise ValueError('The matrix must be rectangular')
    return[[mat[j][i] for j in range(len(mat))] for i in range(row_length)]

def row_sums(mat:list[list[float|int]]) -> list[float]:
    if not mat:
        return[]
    row_length=len(mat[0])

    if any(len(row)!=row_length for row in mat):
        raise ValueError('The matrix must be rectangular')
    return [sum(row) for row in mat]

def col_sums(mat:list[list[float| int]]) -> list [float]:
    if not mat:
        return[]
    row_length=len(mat[0])

    if any(len(row)!=row_length for row in mat):
        raise ValueError ('The matrix must be rectangular')
    return [sum(mat[i][j] for i in range (len(mat))) for j in range(row_length)]

print(transpose([])) # [[1, 4], [2, 5], [3, 6]]
print(row_sums([[-1, 1], [10, -10]])) # [6, 15]
print(col_sums([[1, 2, 3], [4, 5, 6]])) # [5, 7, 9]