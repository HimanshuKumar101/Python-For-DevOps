

count = 1

while count <= 10:
    print("Hello world")
    count += 1


i = 1

while i <= 10:
    if( i % 2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1




#for loop

#loops are used to iterate over a sequence traversal. for traversing list , string , tuple


list = [1,2,3,4,5]

for val in list:
    print(val)


veggies = ["potato", "tomato", "onion"]

for val in veggies:
    print(val)


tup = (1,2,3,4,5)

for num in tup:
    print(num)


string = "Hello World"

for char in string:
    print(char)


#for loop each 


#range functions returns a sequence of numbers, starting from 0 by default , and increments by 1 by default and stops before a specified numbers.

#range(start?,stop,,step?)

for i in range(1,11):
    print(i)
else:
    print("Loop executed successfully")
