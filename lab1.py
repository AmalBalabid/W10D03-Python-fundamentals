

# Task1
num = int(input("Enter a number: "))


flag = False

# prime numbers are greater than 1
if num > 1:

    for i in range(2, num):
        if (num % i) == 0:

            flag = True

            break


if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Task2


def show_student(name, GPA=0):
    print("name: "+name)
    if GPA:
        print("GPA: "+GPA)
    else:
        print(0)


show_student("sarah", "4.90")
show_student("sarah")

# Task3

subjects_grades = {'Physics': 90, 'Math': 100, 'history': 70}

max = subjects_grades["Physics"]
if max < subjects_grades["Math"]:
    max = subjects_grades["Math"]
else:
    if max < subjects_grades['history']:
        max = subjects_grades["history"]

min = subjects_grades["Physics"]
if min > subjects_grades["Math"]:
    min = subjects_grades["Math"]
else:
    if min > subjects_grades['history']:
        min = subjects_grades["history"]


print("Maximum grade is: "+str(max))
print("Minimum grade is: "+str(min))
