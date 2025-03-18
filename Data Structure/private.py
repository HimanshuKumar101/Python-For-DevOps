
#private(like) attribute and methods

#conceptual implementations in python
#private attributes and methods are not meant to be used only withing the class and 
#are not accessible from outside the class

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   #private attribute


# acc = Account("12345", "abcde")

# print(acc.acc_no)
# print(acc.__acc_pass)



class Person:
    __name = "anonymous"


    def __hello(self):
        print("hello person!")


    def welcome(self):
       self. __hello()

p1 = Person()

print(p1.welcome())
