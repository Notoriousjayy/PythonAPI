from sys import float_info
from math import fabs
from math import sqrt
from math import acos
from math import radians
from math import degrees


class Vector(object):
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    @staticmethod
    def dotProduct(left, right):
        return left.x * right.x + left.y * right.y

    @staticmethod
    def addition(left, right):
        return Vector(left.x + right.x, left.y + right.y)

    @staticmethod
    def subtraction(left, right):
        return Vector(left.x - right.x, left.y - right.y)

    @staticmethod
    def multiplication(left, right):
        return Vector(left.x * right.x, left.y * right.y)

    @staticmethod
    def scale(vector, scale):
        return Vector(vector.x * scale, vector.y * scale)

    @staticmethod
    def CMP(x, y):
        return fabs(x - y) <= float_info.epsilon * max(1.0, max(fabs(x), fabs(y)))

    @staticmethod
    def Equality(left, right):
        return Vector.CMP(left.x, right.x) and Vector.CMP(left.y, right.y)

    @staticmethod
    def noEquality(left, right):
        return left != right

    @staticmethod
    def magnitude(vector):
        return sqrt(Vector.dotProduct(vector, vector))

    @staticmethod
    def magnitudeSquareRoot(vector):
        return Vector.dotProduct(vector, vector)

    @staticmethod
    def normalize(vector):
        vector = Vector.scale(vector, (1.0 / Vector.magnitude(vector)))

    @staticmethod
    def normalized(vector):
        magnitude = Vector.magnitude(vector)
        try:
            return Vector.scale(vector, (1.0 / magnitude))
        except ZeroDivisionError:
            return Vector(0, 0)

    # creates a vector from two points
    @staticmethod
    def from_points(point1, point2):
        return Vector(point2[0] - point1[0], point2[1] - point1[1])

    @staticmethod
    def toVector(vector):
        return Vector(vector[0], vector[1])

    @staticmethod
    def angle(left, right):
        m = sqrt(Vector.magnitudeSquareRoot(left) * Vector.magnitudeSquareRoot(right))
        return acos(Vector.dotProduct(left, right) / m)

    @staticmethod
    def radianToDegree(x):
        return radians(x)

    @staticmethod
    def degreeToRadians(x):
        return degrees(x)

    @staticmethod
    def projection(length, direction):
        dot: float = Vector.dotProduct(length, direction)
        magnitudeSquared = Vector.magnitudeSquareRoot(direction)

        return Vector.scale(direction, (dot / magnitudeSquared))

    @staticmethod
    def perpendicular(length, direction):
        new_vector = Vector.projection(length, direction)
        new_vector = Vector.toVector(new_vector)
        return Vector.subtraction(length, new_vector)

    @staticmethod
    def reflection(vector):
        normal_vector = Vector.normalized(vector)
        distance = Vector.dotProduct(vector, normal_vector)
        a = Vector.scale(normal_vector, distance * 2.0)

        return Vector.subtraction(vector, a)