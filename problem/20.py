def transpose_matrix(matrix1):
    num_cols = len(matrix1[0])
    result = []
    for i in range(num_cols):
        result.append([])
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            result[j].append(matrix1[i][j])
    return(result)
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(transpose_matrix(matrix1))