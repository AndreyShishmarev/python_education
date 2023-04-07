class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):

        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                print(self.matrix_list[i][j], end=' ')
            print()
        # return self.matrix_list


mtx = Matrix([[11, 22], [33, 44], [55, 66]])
# print(mtx.matrix_list)
print(mtx)
