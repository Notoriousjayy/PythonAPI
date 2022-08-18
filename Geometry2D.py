import math
from sys import float_info
from math import fabs

from Matrix2 import Matrix2
from Vector2 import Vector

class Point2D(Vector):

    x: float = 0.0
    y: float = 0.0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class LineSegment2D(object):
    start: Point2D
    end: Point2D

    def __init__(self, start: Point2D = Point2D(0, 0), end: Point2D = Point2D(0, 0)):
        self.start = start
        self.end = end

    @staticmethod
    def CMP(x, y):
        return fabs(x - y) <= float_info.epsilon * max(1.0, max(fabs(x), fabs(y)))
    @staticmethod
    def Length(line):
        return Point2D.magnitude(Point2D.subtraction(line.end, line.start))

    @staticmethod
    def LengthSq(line):
        return Point2D.magnitudeSquareRoot(Point2D.subtraction(line.end, line.start))

    @staticmethod
    def PointOnLineSegment(point: Point2D, line):
        dy: float = line.end.y - line.start.y
        dx: float = line.end.x - line.start.x
        M: float = dy / dx

        # Find the Y-Intercept
        B: float = line.start.y - M * line.start.x


        # Check line equation
        return Point2D.CMP(point.y,M * point.x + B)

class Circle(object):
    position: Point2D
    radius: float

    def __init__(self, point: Point2D = Point2D(0, 0), radius: float = 1.0):
        self.position = point
        self.radius = radius

    @staticmethod
    def PointInCircle(point: Point2D, circle):
        line: LineSegment2D = LineSegment2D(point, circle.position)
        LineSegment2D.LengthSq(line)
        if LineSegment2D.LengthSq(line) < math.pow(circle.radius, 2):
            return True
        return False

class Rectangle(object):
    origin: Point2D
    size: Vector

    def __init__(self, origin:Point2D = Point2D(0, 0), size = Vector(1, 1)):
        self.origin = origin
        self.size = size

    @staticmethod
    def GetMinPoints(rectangle):
        point1: Vector = rectangle.origin
        point2: Vector = Point2D.addition(rectangle.origin, rectangle.size)

        return Vector(min(point1.x, point2.x), min(point1.y, point2.y))

    @staticmethod
    def GetMaxPoints(rectangle):
        point1: Vector = rectangle.origin
        point2: Vector = Point2D.addition(rectangle.origin, rectangle.size)

        return Vector(max(point1.x, point2.x), max(point1.y, point2.y))

    @staticmethod
    def FromMinMaxPoints(min: Vector, max: Vector):
        return Rectangle(min, Point2D.subtraction(max, min))

    @staticmethod
    def PointInRectangle(point: Point2D, rectangle):
        min: Vector = Rectangle.GetMinPoints(rectangle)
        max: Vector = Rectangle.GetMaxPoints(rectangle)

        return  min.x <= point.x and min.y <= point.y and point.x <= max.x and point.y <= max.y

class OrientedRectangle(object):
    position: Point2D
    halfExtents: Vector
    rotation: float

    def __init__(self, position: Point2D = Point2D(0.0), halfExtents: Vector = Vector(1.0, 1.0), rotation: float = 0.0):
        self.position = position
        self.halfExtents = halfExtents
        self.rotation = rotation

    @staticmethod
    def PointInOrientedRectangle(point: Point2D, rectangle):
        rotVevtor: Vector = Vector.subtraction(point, rectangle.position)
        theta: float = -Vector.degreeToRadians(rectangle.rotation)
        zRotation = Matrix2.asArray(Matrix2(math.cos(theta), math.sin(theta), -math.sin(theta), math.cos(theta)))

        Matrix2.Multuply(Matrix2.asArray(rotVevtor), list(Vector(rotVevtor.x, rotVevtor.y)), 1, 2, zRotation, 2 , 2)