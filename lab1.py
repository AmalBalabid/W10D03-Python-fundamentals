
#---------------------Task 1-------------------

number1 = input("please enter start number: ")
number2 = input("please enter end number: ")

start = int(number1)
end = int(number2)
test = start

for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)


#---------------------Task 2-------------------

name = input("please enter name: ")
gpa = input("please enter GPA: ")


def show_student(name, gpa=0):
   
    print("your name: ", name)

    if gpa:
         print("your GPA: ", gpa)
    else:
        print("your GPA: 0")

show_student(name,gpa)

#---------------------Task 3-------------------

subjects_grades = { 
    'Physics': 90, 
    'Math': 100, 
    'history': 70 
    }

max = max(subjects_grades, key = subjects_grades.get)
min = min(subjects_grades, key = subjects_grades.get)
print("Max grade is " + max)
print("Min grade is " + min)


