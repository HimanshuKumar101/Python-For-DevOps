marks = [94.4, 64,55,89,55]

print(marks)
print(marks[0])
print(marks[-1])

student = ["Himanshu", 23, 94.4, "Btech"]

#list are mutable

print(student)
student[3] = "MCA"

print(student)


print(marks[1:4])

student.append("Noida")

print(student)

student.insert(2, "Kumar")

print(student)

marks.sort()

print(marks)

marks.reverse()

print(marks)

marks.pop()

marks.pop()

print(marks)