import math
from sys import float_info
from math import fabs


from Matrix2 import Matrix2


class Matrix3(object):
    _11: float
    _12: float
    _13: float
    _21: float
    _22: float
    _23: float
    _31: float
    _32: float
    _33: float

    def __init__(self, _11=1.0, _12=0.0, _13=0.0, _21= 0.0, _22=1.0, _23=0.0, _31=0.0, _32=0.0, _33=1.0):
        self._11 = _11
        self._12 = _12
        self._13 = _13
        self._21 = _21
        self._22 = _22
        self._23 = _23
        self._31 = _31
        self._32 = _32
        self._33 = _33

    def __str__(self):
        return "%s\t\t%s\t\t%s\n%s\t\t%s\t\t%s\n%s\t\t%s\t\t%s" % (self._11, self._12, self._13, self._21, self._22, self._23, self._31, self._32, self._33)

    @staticmethod
    def asArray(matrix):
        Array = list()
        Array.append(matrix._11)
        Array.append(matrix._12)
        Array.append(matrix._13)
        Array.append(matrix._21)
        Array.append(matrix._22)
        Array.append(matrix._23)
        Array.append(matrix._31)
        Array.append(matrix._32)
        Array.append(matrix._33)

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
    def TransposeMatrix3(matrix):
        result = Matrix3()
        result = Matrix3.Transpose(Matrix3.asArray(matrix), Matrix3.asArray(result), 3, 3)
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

    @staticmethod
    def ScalarMultiplication(matrix, sclar: float):
        result = list()
        matrix = Matrix3.asArray(matrix)
        for i in range(9):
            result.append(matrix[i] * sclar)
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

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
        result = [0 for item in range(9)]
        matrixAList = Matrix3.asArray(matrixA)
        matrixBList = Matrix3.asArray(matrixB)
        Matrix3.Multuply(result, matrixAList, 3, 3, matrixBList, 3, 3)
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

    @staticmethod
    def Cut(matrix, row, column):
        result = [0 for item in range(9)]
        index = 0
        matrix = Matrix3.asArray(matrix)
        for i in range(3):
            for j in range(3):
                if i == row or j == column:
                    continue
                target = index
                index += 1
                source = 3 * i + j
                result[target] = matrix[source]

        return Matrix2(result[0], result[1], result[2], result[3])

    @staticmethod
    def Minor(matrix):
        result = [[0] * 3] * 3
        temp = list()
        for i in range(3):
            for j in range(3):
                result[i][j] = Matrix2.Determinant(Matrix3.Cut(matrix, i , j))
            temp.extend(result[0])
        result = temp
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

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
        result = [0 for item in range(9)]
        minor = Matrix3.asArray(Matrix3.Minor(matrix))
        Matrix3.Cofactor(result, minor, 3, 3)
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

    @staticmethod
    def DeterminantLaplaceExpnasion(matrix):
        result = 0.0
        cofactor = Matrix3.asArray(Matrix3.CofactorMatrix(matrix))
        cofactor = [cofactor[i:i+3] for i in range(0, len(cofactor), 3)]
        matrix = Matrix3.asArray(matrix)
        for j in range(3):
            index = 3 * 0 + j
            result += matrix[index] * cofactor[0][j]
        return result

    @staticmethod
    def Adjugate(matrix):
        return Matrix3.TransposeMatrix3(Matrix3.CofactorMatrix(matrix))

    @staticmethod
    def Inverse(matrix):
        determinant = Matrix3.DeterminantLaplaceExpnasion(matrix)
        if Matrix3.CMP(determinant, 0.0):
            pass
        return Matrix3.ScalarMultiplication(Matrix3.Adjugate(matrix), (1.0 / determinant))