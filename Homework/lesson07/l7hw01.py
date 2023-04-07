class Matrix:
    n = int
    m = int

    def __init__(self, n, m):
        self.n = n
        self.m = m
        matrix_list = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(input())
            matrix_list.append(row)

        for t in range(n):
            for k in range(m):
                print(matrix_list[t][k], end=' ')
            print()


matrix = Matrix(3, 3)
