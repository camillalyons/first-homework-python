##Classes: Dealing with Complex Numbers
class Complex(object):
    def __init__(self, real, imaginary):
        self.real= real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.imaginary*no.real+self.real*no.imaginary)
    def __truediv__(self, no):
        return Complex(((self.real*no.real+self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2)), (self.imaginary*no.real-self.real*no.imaginary)/(no.real**2+no.imaginary**2))
    def mod(self):
        return Complex(round(pow((self.real**2 + self.imaginary**2), 0.5), 2), 0.0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

##Class 2 - Find the Torsional Angle
import math
class Points(object):
    def __init__(self, x, y, z):
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
    def __sub__(self, no):
            return Points(self.x-no.x, self.y-no.y, self.z-no.z)
    def dot(self, no):
            return self.x*no.x + self.y*no.y + self.z*no.z
    def cross(self, no):
            return Points(self.y*no.z-self.z*no.y, self.z*no.x-self.x*no.z, self.x*no.y-self.y*no.x)
    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)