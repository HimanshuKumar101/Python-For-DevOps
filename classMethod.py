#class method

""""

a class method is bound to the class and receives the class as an implicit first argument.

note- static method can't access or modify class state and generally for utility



"""

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     #self.name = name
    #     #Person.name = name

    #     self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("himanshu")
print(p1.name)

print(Person.name)