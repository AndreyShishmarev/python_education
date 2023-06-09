class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                matrix_sum = self.matrix_list + other.matrix_list
                result.append(matrix_sum)
                # print(self.matrix_list[i][j], end=' ')
            print(result)
        return Matrix(result)

    def __str__(self):
        return f"Матрица:\n{' '.join(map(str, self.matrix_list))} \n{' '.join(map(str, self.matrix_list[1]))} \n" \
               f"{' '.join(map(str, self.matrix_list[2]))} \n "


mtx1 = Matrix([[11, 22], [33, 44], [55, 66]])
mtx2 = Matrix([[20, 30], [40, 50], [60, 70]])
mtx_sum = mtx1 + mtx2
print(mtx_sum)
# result = map(sum, zip(mtx1,mtx2))
