import array;

arr = array.array('i',[1,2,3])

print(arr)

arr.append(10)  #append element at the end

print(arr)

arr.pop()   #removes last element

print(arr)


print(arr[0])   #indexing bases accessing element 

print(arr[0:1])  #slicing


for i in range(0,2):
    arr.pop()
    print(arr)