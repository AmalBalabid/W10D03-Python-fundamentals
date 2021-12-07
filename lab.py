# Task 1:
# Write a program to display all prime numbers within a range spcified by user input
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

# Examples:
# 10 is not a prime number because it can be made by 2×5 = 10
# 11 is a prime number because no other whole numbers multiply together to make it.
# Given range: start = 50 end = 100
# Expected output: Prime numbers between 25 and 50 are: 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

start_time = input("Enter start time: ")
end_time = input("Enter end time: ")
print("Prime number in range: "+start_time+"-"+end_time)
for i in range(int(start_time), int(end_time)+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
               break
        else:
           print(i)

# Task 2:
# Write a program to create a function show_student() using the following conditions.

# It should accept the student’s name and GPA and display both.
# If the GPA is missing in the function call then assign default value 0 to GPA
def show_student(student_name, GPA=0):
    print("Student Name:",student_name)
    print("GPA:",GPA)
show_student("shrooq",4.8)

# Task 3:
# Write a program to create a dictionary including subjects and grades then print the key of the minimum and maximum grades.
# subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
# Expected output: Minimum grade is history Maximum grade is Math

subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
max_key = max(subjects_grades, key=subjects_grades.get)
min_key = min(subjects_grades, key=subjects_grades.get)

print("Minimum grade is "+min_key+" and Maximum grade is "+max_key)
