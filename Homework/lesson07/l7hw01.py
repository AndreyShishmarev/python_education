class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                print(self.matrix_list[i][j], end=' ')
            print()
    # def __str__(self):
    #
    #     return

    # def __add__(self, other):
    #     return Matrix(self.matrix_list + other.matrix_list)


mtx1 = Matrix([[11, 22], [33, 44], [55, 66]])
mtx2 = Matrix([[12, 23], [34, 45], [56, 67]])
# mtx = mtx1 + mtx2
# print(mtx.matrix_list)
# print(mtx)
