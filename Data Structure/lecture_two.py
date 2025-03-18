str1 = "This is a string.\nwe are creating it in python." #escape sequence for nxt line


print(str1)

name = "Himanshu "
last_name ="Kumar"

print(name + last_name)


print(len(name))

print(name[0])

print(name[0:3])  #ending idx is not included


#negative index

print(name[-5:-2])

#String functions

str = "i am studying python from apnaCollege"

print(str.endswith("er"))

print(str.capitalize())


#conditon

light = "orange"

if(light == "red"):
    print("stop")
elif( light == "green"):
    print("go")
else:
    print("get ready")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if( a >= b and a >= c):
    print("First number is largest")
elif(b >= c):
    print("Second number is largest")
else:
    print("third number is largest")



