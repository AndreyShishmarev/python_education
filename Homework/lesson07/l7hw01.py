class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        return Matrix(self.matrix_list + other.matrix_list)

    def __str__(self):
        result = ''
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                print(self.matrix_list[i][j], end=' ')
            print()
        return result


mtx1 = Matrix([[11, 22], [33, 44], [55, 66]])
mtx2 = Matrix([[20, 30], [40, 50], [60, 70]])
mtx_sum = mtx1 + mtx2
print(mtx_sum)
# result = map(sum, zip(mtx1,mtx2))
