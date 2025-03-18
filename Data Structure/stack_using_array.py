import array

class Stack:
    def __init__(self):
        self.my_stack = array.array('i',[])

        self.top = -1



#self is the current object of the class
#self.my stack is the array that will be used to store the stack element 

    def push(self,element): #push element to the stack function 
        self.my_stack.append(element) #append element at the end of the stack array
    
    def get_top(self):
        return len(self.my_stack)-1

    def is_empty(self):
        if len(self.my_stack):
            return False
        else:
            return True

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self.my_stack.pop()


if __name__ == "__main__":  #main function in python stars from here
    stack = Stack() #object in python

    stack.push(1)
    print(stack.top)
    stack.push(2)
    stack.push(3)

    print(stack.my_stack)

    stack.pop()
    print(stack.my_stack)
