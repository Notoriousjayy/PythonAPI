import math
from sys import float_info
from math import fabs

from Matrix2 import Matrix2
from Matrix3 import Matrix3


class Matrix4(object):
    _11: float
    _12: float
    _13: float
    _14: float
    _21: float
    _22: float
    _23: float
    _24: float
    _31: float
    _32: float
    _33: float
    _34: float
    _41: float
    _42: float
    _43: float
    _44: float

    def __init__(self, _11=1.0, _12=0.0, _13=0.0, _14=0.0, _21= 0.0, _22=1.0, _23=0.0, _24=0.0, _31=0.0, _32=0.0, _33=1.0, _34=0.0, _41=0.0, _42=0.0, _43=0.0, _44=1.0):
        self._11 = _11
        self._12 = _12
        self._13 = _13
        self._14 = _14
        self._21 = _21
        self._22 = _22
        self._23 = _23
        self._24 = _24
        self._31 = _31
        self._32 = _32
        self._33 = _33
        self._34 = _34
        self._41 = _41
        self._42 = _42
        self._43 = _43
        self._44 = _44

    def __str__(self):
        return "%s\t\t%s\t\t%s\t\t%s\n%s\t\t%s\t\t%s\t\t%s\n%s\t\t%s\t\t%s\t\t%s\n%s\t\t%s\t\t%s\t\t%s" % (self._11, self._12, self._13, self._14, self._21, self._22, self._23,self._24, self._31, self._32, self._33, self._34, self._41, self._42, self._43, self._44)

    def asArray(matrix):
        Array = list()
        Array.append(matrix._11)
        Array.append(matrix._12)
        Array.append(matrix._13)
        Array.append(matrix._14)
        Array.append(matrix._21)
        Array.append(matrix._22)
        Array.append(matrix._23)
        Array.append(matrix._24)
        Array.append(matrix._31)
        Array.append(matrix._32)
        Array.append(matrix._33)
        Array.append(matrix._34)
        Array.append(matrix._41)
        Array.append(matrix._42)
        Array.append(matrix._43)
        Array.append(matrix._44)

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
    def TransposeMatrix4(matrix):
        result = Matrix4()
        result = Matrix4.Transpose(Matrix4.asArray(matrix), Matrix4.asArray(result), 4, 4)
        return Matrix4(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])

    @staticmethod
    def ScalarMultiplication(matrix, sclar: float):
        result = list()
        matrix = Matrix4.asArray(matrix)
        for i in range(16):
            result.append(matrix[i] * sclar)
        return Matrix4(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])

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
        result = [0 for item in range(16)]
        matrixAList = Matrix4.asArray(matrixA)
        matrixBList = Matrix4.asArray(matrixB)
        Matrix4.Multuply(result, matrixAList, 4, 4, matrixBList, 4, 4)
        return Matrix4(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])

    @staticmethod
    def Cut(matrix, row, column):
        result = [0 for item in range(9)]
        index = 0
        matrix = Matrix4.asArray(matrix)
        for i in range(4):
            for j in range(4):
                if i == row or j == column:
                    continue
                target = index
                index += 1
                source = 4 * i + j
                result[target] = matrix[source]
        # print(Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))
        # print()
        return Matrix3(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

    @staticmethod
    def Minor(matrix):
        result = [[0] * 4] * 4
        temp = list()
        # print(matrix)
        for i in range(4):
            for j in range(4):
                # print("(i: ", i , "," "j: ", j , ")")
                result[i][j] = Matrix3.DeterminantLaplaceExpnasion(Matrix4.Cut(matrix, i, j))
                # print(result[i][j])
            temp.extend(result[0])
        result = temp
        return Matrix4(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])

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
        result = [0 for item in range(16)]
        minor = Matrix4.asArray(Matrix4.Minor(matrix))
        Matrix4.Cofactor(result, minor, 4, 4)
        return Matrix4(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])

    @staticmethod
    def DeterminantLaplaceExpnasion(matrix):
        result = 0.0
        cofactor = Matrix4.asArray(Matrix4.CofactorMatrix(matrix))
        cofactor = [cofactor[i:i+4] for i in range(0, len(cofactor), 4)]
        matrix = Matrix4.asArray(matrix)
        for j in range(4):
            index = 4 * 0 + j
            result += matrix[index] * cofactor[0][j]
        return result

    @staticmethod
    def Adjugate(matrix):
        return Matrix4.TransposeMatrix4(Matrix4.CofactorMatrix(matrix))

    @staticmethod
    def Inverse(matrix):
        determinant = Matrix4.DeterminantLaplaceExpnasion(matrix)
        if Matrix4.CMP(determinant, 0.0):
            pass
        return Matrix4.ScalarMultiplication(Matrix4.Adjugate(matrix), (1.0 / determinant))