
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, number):
        return Complex(self.real + number.real, self.imaginary + number.imaginary)
        
    def __sub__(self, number):
        return Complex(self.real - number.real, self.imaginary - number.imaginary)
        
    def __mul__(self, number):
        return Complex(self.real * number.real - self.imaginary * number.imaginary, self.real * number.imaginary + self.imaginary * number.real)

    def __truediv__(self, number):
        return Complex((self.real * number.real + self.imaginary * number.imaginary)/(number.real**2 + number.imaginary**2), (self.imaginary * number.real - self.real * number.imaginary)/(number.real**2 + number.imaginary**2))

    def __mod__(self, number):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

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

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x % y, y % x]), sep='\n')
