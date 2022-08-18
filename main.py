#!/usr/bin/env python
import Geometry2D
from Vector2 import Vector
from Matrix2 import Matrix2
from Matrix3 import Matrix3
from Matrix4 import Matrix4
from Geometry2D import Point2D
from Geometry2D import LineSegment2D
from Geometry2D import Circle
from Geometry2D import Rectangle

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # A = Vector(10, 20)
    # B = Vector(30, 35)
    # C = Vector(10, 20)
    # D = Vector(35, 50)
    #
    # p1 = Vector.perpendicular(A, B)
    # p2 = Vector.perpendicular(A, C)
    point1 = Point2D(1.0, 3.0)
    point2 = Point2D(7.0, -3.0)
    point3 = Point2D(27.0, -33.0)

    circle1 = Circle()
    circle2 = Circle(point1, 5)
    # print(Circle.PointInCircle(point1, circle2))
    # print(circle1)
    # # print(circle2)
    # rectangle = Rectangle()
    rectangle1 = Rectangle.FromMinMaxPoints(Vector(0, 0), Vector(50, 50))
    print(rectangle1)
    print(Rectangle.GetMinPoints(rectangle1))
    print(Rectangle.GetMaxPoints(rectangle1))

    print(Rectangle.PointInRectangle(point3, rectangle1))
    # print(point1)
    # print(point2)
    # print(Point2D.magnitude(Vector.toVector(Point2D.subtraction(point1, point2))))
    line = LineSegment2D(point1, point2)
    line1 = LineSegment2D()
    # print(LineSegment2D.PointOnLineSegment(point3, line))
    print(LineSegment2D.LengthSq(line1))
    print(LineSegment2D.LengthSq(line))
    #
    # print(Vector.reflection(A))
    # print(Vector.reflection(B))
    # print(Vector.reflection(C))
    # print(Vector.reflection(D))
    #
    # m2 = Matrix2()
    m22 = Matrix2(3, 7, 5, 9)
    print(m22)
    # print()
    print(Matrix2.Inverse(m22))
    print()
    print(Matrix2.Adjugate(m22))
    print()
    print(Matrix2.CofactorMatrix(m22))
    print()
    # print()
    print(Matrix2.Determinant(m22))
    print()
    print(Matrix2.Minor(m22))
    print()
    # print(m2)
    # print()
    # print(m22)
    # print()

    # m2 = Vector.MatrixToVextor(m2)
    # m22 = Vector.MatrixToVextor(m22)
    # sum = 0
    # for _ in range(4):
    #     sum += Vector.dotProduct(m2, m22)
    # print(sum)
    # print()
    # print(Matrix2.MultiplyMatrix(m2, m22))
    #
    # print(Matrix2.TransposeMatrix2(m2))
    # print()
    # print(Matrix2.ScalarMultiplication(m2, 1000))

    # m3 = Matrix3()
    # m33 = Matrix3(3, 7, 5, 9, 2, 1, 4, 6, 2)
    # m33 = Matrix3(1, 8, 7, 3, 9, 5, 1, 0, 4)
    # print(Matrix3.CofactorMatrix(m33))
    # print(Matrix3.DeterminantLaplaceExpnasion(m33))
    # print()
    # print(m3)
    # print()
    # print(m33)
    # print()
    # print(Matrix3.Inverse(m33))
    # print(Matrix3.Adjugate(m33))
    # print(Matrix3.MultiplyMatrix(m3, m33))
    # print()
    # print(Matrix3.Minor(m33))
    #
    # print(Matrix3.TransposeMatrix3(m3))
    # print()
    # print(Matrix3.ScalarMultiplication(m3, 1000))


    # print(Matrix3.MultiplyMatrix(m3, m33))

    # m4 = Matrix4(1.0, 0.0, 1.0, 3.0, 9.9, 8.8, 7.7, 6.6, 5.5, 8.4, 5.6, 4.5, 4.5, 4.6, 7.5, 4.6)
    # m44 = Matrix4(1, 0, 3, 1, 9, 8, 7, 6, 5, 8, 5, 4, 4, 4, 7, 4)
    # print(m44)
    # print()
    # print(Matrix4.Inverse(m44))
    # print(Matrix4.Adjugate(m44))
    # print(Matrix4.Minor(m44))
    # print(Matrix4.DeterminantLaplaceExpnasion(m44))
    # m4 = Matrix4()
    # m44 = Matrix4()
    # print(m4)
    # print()
    # print(Matrix4.TransposeMatrix4(m4))
    #
    # print()
    # print(Matrix4.ScalarMultiplication(m4, 1000))
    # print(Matrix4.MultiplyMatrix(m4, m44))
    # print(Matrix4.Minor(m44))