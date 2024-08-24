


# Write a program that can check if you can perform matrix multiplication on 2 matrices 
matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

rows_a = len(matrix_a)
cols_a = len(matrix_a[0])
rows_b = len(matrix_b)
cols_b = len(matrix_b[0])
if cols_a == rows_b:
    print("Matrix multiplication is possible.")
else:
    print("Matrix multiplication is not possible.")
