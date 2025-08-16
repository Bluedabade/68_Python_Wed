def sum_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        result_sum = []
        for j in range (len(matrix1[i])):
            total = matrix1[i][j] + matrix2[i][j] 
            result_sum.append(total)
        result.append(result_sum)
    return(result)

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1]]

print(sum_matrices(matrix1, matrix2))