#inheritance
#when one class(child/derived) derives the properties and methods of another class( parent/base).

""" 
types of inheritance:
1. single inheritance
2. multiple inheritance
3. multilevel inheritance
"""



""""

class Car:
    @staticmethod
    def start():
        print("Car started...")

    
    @staticmethod
    def stop():
        print("Car stopped...")


class Audi(Car): 
    def __init__(self, name):
        self.name = name


class Fortuner(Audi):
    def __inti__(self, name):
        self.type = type


Car1 = Audi("Audi")
print(Car1.name)
print(Car1.start())

car1 = Fortuner("Fortuner Legender")
print(car1.name)


"""

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC) 

#Super method


