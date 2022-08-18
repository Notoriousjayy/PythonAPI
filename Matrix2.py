import math
from sys import float_info
from math import fabs

class Matrix2(object):
    _11: float
    _12: float
    _21: float
    _22: float

    def __init__(self, _11=1.0, _12=0.0, _21=0.0, _22=1.0):
        self._11 = _11
        self._12 = _12
        self._21 = _21
        self._22 = _22

    def __str__(self):
        return "%s\t\t%s\n%s\t\t%s" % (self._11, self._12, self._21, self._22)

    @staticmethod
    def asArray(matrix):
        Array = list()
        Array.append(matrix._11)
        Array.append(matrix._12)
        Array.append(matrix._21)
        Array.append(matrix._22)

        return Array

    @staticmethod
    def CMP(x, y):
        return fabs(x - y) <= float_info.epsilon * max(1.0, max(fabs(x), fabs(y)))

    @staticmethod
    def Transpose(sourceMatrix, destinationMatrix, sourceRows, sourceColumns):
        for i in range(sourceRows * sourceColumns):
            row = i / sourceRows
            column = i % sourceRows
            destinationMatrix[i] = sourceMatrix[int(sourceColumns * column + row)]
        return destinationMatrix

    @staticmethod
    def TransposeMatrix2(matrix):
        result = Matrix2()
        result = Matrix2.Transpose(Matrix2.asArray(matrix), Matrix2.asArray(result), 2, 2)
        return Matrix2(result[0], result[1], result[2], result[3])

    @staticmethod
    def ScalarMultiplication(matrix, sclar: float):
        result = list()
        matrix = Matrix2.asArray(matrix)
        for i in range(4):
            result.append(matrix[i] * sclar)
        return Matrix2(result[0], result[1], result[2], result[3])

    @staticmethod
    def Multuply(out, matrixA, aRows, aColumns, matrixB, bRows, bColumns):
        if aColumns != bRows:
            return False

        for i in range(aRows):
            for j in range(bColumns):
                out[bColumns * i + j] = 0.0
                for k in range(bRows):
                    a = aColumns * i + k
                    b = bColumns * k + j
                    out[bColumns * i + j] += matrixA[a] * matrixB[b]

        return True

    @staticmethod
    def MultiplyMatrix(matrixA, matrixB):
        result = [0 for item in range(4)]
        matrixAList = Matrix2.asArray(matrixA)
        matrixBList = Matrix2.asArray(matrixB)
        Matrix2.Multuply(result, matrixAList, 2, 2, matrixBList, 2, 2)
        return Matrix2(result[0], result[1], result[2], result[3])

    @staticmethod
    def Determinant(matrix):
        return matrix._11 * matrix._22 - matrix._12 * matrix._21

    @staticmethod
    def Minor(matrix):
        return Matrix2(matrix._22, matrix._21, matrix._12, matrix._11)

    @staticmethod
    def Cofactor(out, minor, rows, columns):
        for i in range(rows):
            for j in range(columns):
                t = columns * j + i # Target index
                s = columns * j + i # Source index
                sign = math.pow(-1.0, i+j)
                out[t] = minor[s] * sign

    @staticmethod
    def CofactorMatrix(matrix):
        result = [0 for item in range(4)]
        minor = Matrix2.asArray(Matrix2.Minor(matrix))
        Matrix2.Cofactor(result, minor, 2, 2)
        return Matrix2(result[0], result[1], result[2], result[3])

    @staticmethod
    def Adjugate(matrix):
        return Matrix2.TransposeMatrix2(Matrix2.CofactorMatrix(matrix))


    @staticmethod
    def Inverse(matrix):
        determinant = Matrix2.Determinant(matrix)
        if Matrix2.CMP(determinant, 0.0):
            pass
        return Matrix2.ScalarMultiplication(Matrix2.Adjugate(matrix), (1.0 / determinant))
