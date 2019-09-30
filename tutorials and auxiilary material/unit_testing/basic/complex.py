class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __sub__(self, other):
        return self + -other

    def congugate(self):
        return Complex(self.real, -self.other)

    def __mul__(self, other):
        if isinstance(other, Complex):
            r = self.real * other.real - self.img * other.img
            i = self.real * other.img + self.img * other.real
        else:
            r = self.real * other
            i = self.img * other
        return Complex(r, i)


    def __div__(self, other):
        if isinstance(other, Complex):
            numer = self * other.congugate()
            denom = other * other.congugate
            denom = denom.real
            return Complex(numer.real / denom, numer.img / denom )
        return Complex(numer.real / other, numer.img / other)
