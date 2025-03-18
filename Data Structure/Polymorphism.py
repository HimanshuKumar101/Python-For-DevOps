#polymorphism: Operator overloading

#when the same operator is allowed to have different meaning according to the context, it is called operator overloading.

class Complex:
        def __init__(self, real, img):
            self.real = real
            self.img = img

        def showNumber(self):
            print(self.real, "i +", self.img,"j")

        def __add__(self, num2):
            newReal = self.real + num2.real
            newImg = self.img + num2.img
            return Complex(newReal, newImg)
        
        def __sub__(self, num2):
            newReal = self.real - num2.real
            newImg = self.img - num2.img
            return Complex(newReal, newImg)


num1 = Complex(3, 4)

num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

#num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

"""
Operators & Dunder functions

Operator	Expression	Internally
a + b	__add__(self, other)	a.__add__(b)
a - b	__sub__(self, other)	a.__sub__(b)
a * b	__mul__(self, other)	a.__mul__(b)
a / b	__truediv__(self, other)	a.__truediv__(b)
a // b	__floordiv__(self, other)	a.__floordiv__(b)
a % b	__mod__(self, other)	a.__mod__(b)
a ** b	__pow__(self, other)	a.__pow__(b)


"""