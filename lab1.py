# Task1

from typing import AsyncGenerator


print("Enter first number ")
a = int(input())
print("Enter second number ")
b = int(input())

print("Prime numbers")
for i in range(a, b + 1):
 
    if (i == 1):
        continue
    flag = 1    
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break
    if (flag == 1):
        print(i,  " ")

# Task2


def show_student(name,gpa):
    print("The name is : "+name+" the GPA is",gpa)

show_student("amal",4)

# Task3

subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }

if subjects_grades["Math"]>subjects_grades["Physics"]:
    if subjects_grades["Physics"]>subjects_grades["history"]:
        print ("max is Math , min is hestory")
    else:
        print ("max is MAth , min is Phisics")
else:
    if subjects_grades["Math"]>subjects_grades["history"] :
        print("max is Physics , min is Hestory")
    elif subjects_grades["history"]>subjects_grades["Physics"] :
        print("max is history, min is Math")
    else:
        print("max is Physics , min is math")


    






