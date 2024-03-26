import threading
from concurrent.futures import ThreadPoolExecutor


class Matrix:
    def __init__(self, n, m):
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def setMatrix(self, elems):
        n = len(self.matrix)
        m = len(self.matrix[0])
        for i in range(n):
            for j in range(m):
                self.matrix[i][j] = elems[i * n + j]

    def addRow(self, n, row):
        if len(self.matrix[0]) != len(row) or n >= len(self.matrix):
            return
        for i in range(len(self.matrix[0])):
            self.matrix[n][i] = row[i]

    def get_elem(self, i, j):
        return self.matrix[i][j]

    def __getitem__(self, n):
        return self.matrix[n]

    def __eq__(self, m2):
        if len(self.matrix) != m2.rows() or len(self.matrix[0]) != m2.cols():
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if m2.get_elem(i, j) != self.matrix[i][j]:
                    return False
        return True

    def __mul__(self, m2):
        return self.MatrixMul(self, m2)

    def Mul(self, m2):
        return self.MatrixMul(self, m2)

    def print(self):
        for row in self.matrix:
            print(" ".join(str(elem) for elem in row))

    def make_random(self):
        import random
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = random.randint(0, 999)

    def rows(self):
        return len(self.matrix)

    def cols(self):
        return len(self.matrix[0])

    @staticmethod
    def MatrixMul(m1, m2):
        N = m1.cols()
        M = m1.rows()
        Q = m2.cols()
        c = Matrix(M, Q)

        for i in range(M):
            for j in range(Q):
                for k in range(N):
                    c[i][j] += m1[i][k] * m2[k][j]

        return c

    @staticmethod
    def first(MulH, A, N, start, end):
        for i in range(start, end):
            for k in range(0, N - 1, 2):
                MulH[i] -= A[i][k] * A[i][k + 1]

    @staticmethod
    def second(MulV, B, N, start, end):
        for i in range(start, end):
            for k in range(0, N - 1, 2):
                MulV[i] -= B[k][i] * B[k + 1][i]

    @staticmethod
    def third(c, A, B, N, MulH, MulV, starti, endi, startj, endj):
        for i in range(starti, endi):
            for j in range(startj, endj):
                buf = MulH[i] + MulV[j]
                for k in range(0, N - 1, 2):
                    buf += (A[i][k] + B[k + 1][j]) * (A[i][k + 1] + B[k][j])
                if N % 2 == 1:
                    buf += A[i][N - 1] * B[N - 1][j]
                c[i][j] = buf

    # def Mul2(self, A, B):
    #     N = A.cols()
    #     M = A.rows()
    #     Q = B.cols()
    #     c = Matrix(M, Q)
    #
    #     MulH = [0] * M
    #     MulV = [0] * Q
    #
    #     th_1_1 = threading.Thread(target=self.first, args=(MulH, A, N, 0, M))
    #     th_2_1 = threading.Thread(target=self.second, args=(MulV, B, N, 0, Q))
    #
    #     th_1_1.start()
    #     th_2_1.start()
    #
    #     th_1_1.join()
    #     th_2_1.join()
    #
    #     th_3_1 = threading.Thread(target=self.third,
    #                               args=(c, A, B, N, MulH, MulV, 0, M // 2, 0, Q))
    #     th_3_2 = threading.Thread(target=self.third,
    #                               args=(c, A, B, N, MulH, MulV, M // 2, M, 0, Q))
    #
    #     th_3_1.start()
    #     th_3_2.start()
    #
    #     th_3_1.join()
    #     th_3_2.join()
    #     return c

    def Mul2(self, A, B):
        N = A.cols()
        M = A.rows()
        Q = B.cols()
        c = Matrix(M, Q)

        MulH = [0] * M
        MulV = [0] * Q

        with ThreadPoolExecutor(max_workers=3) as executor:
            future_first = executor.submit(self.first, MulH, A, N, 0, M)
            future_second = executor.submit(self.second, MulV, B, N, 0, Q)

            future_first.result()
            future_second.result()

            future_third_1 = executor.submit(self.third, c, A, B, N, MulH, MulV, 0, M // 2, 0, Q)
            future_third_2 = executor.submit(self.third, c, A, B, N, MulH, MulV, M // 2, M, 0, Q)

            future_third_1.result()
            future_third_2.result()

        return c
