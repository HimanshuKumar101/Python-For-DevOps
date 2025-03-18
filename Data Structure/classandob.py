class student:
    college_name = "VIT Bhopal"
    name = "anonymous" #class attribute 

    def __init__(self, name, marks):
        self.name = name    #obj attr > class attr
        self.marks = marks
    
    def welcome(self):
        print("welcome himanshu to python lecture")


#methods that don't use the self parameter( work at class level)'
    @staticmethod    #decorator
    def greet():
        print("good morning " )


#decorators allow us to wrap another function in order to extend the behaviour of the wrapped funcation, without permanently modifying it 


s1 = student("himanshu", 101)
print(s1.name, s1.marks, s1.college_name)

s2 = student("sachin", 102)
print(s2.name, s2.marks, s2.college_name)


#methods are functions that belong to objects

#class consists of attributes and methods
#attributes are variables that belong to objects
#methods are functions that belong to objects

s1.welcome()


s1.greet()
