

#dictionaries are used to store data values in key:value pairs

#they are unordered, mutable (changeable) & don't allow duplicate keys

info = {
    "key" : "value",
    "subjects": ["Python","Java","Linus"],
    "name" : "Himanshu",
    "age": 23
}

print(info)

print(info["name"])

#nested dictonary

student = {
    "name": "Himanshu",
    "age": 23,
    "marks": {
        "maths": 94.4,
        "english": 64,
        "science": 55
    }
}

print(student)


print(student.get("name"))

print(student.keys())

student.update({"city": "Noida"})

print(student)
