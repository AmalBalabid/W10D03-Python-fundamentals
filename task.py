# # //Write a program to display all prime numbers within a range spcified by user input
number1 = int(input("Enter lower number : "))  
number2 = int(input("Enter upper number : "))  
print("Prime numbers between", number1, "and", number2, "are:")
for number in range(number1,number2 + 1):  
   if number > 1:  
       for i in range(2,number):  
           if (number % i) == 0:  
             
               break 

       else:  
           print(number) 
          
#     # ------------------------------------------------

#     # Write a program to create a function show_student() using the following conditions.
def show_student(name,GPA=0):
    print(name,GPA)

show_student("GHADEER")

#  # ------------------------------------------------

# Write a program to create a dictionary including subjects
#   and grades then print the key of the minimum and maximum grades.

subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }


print('Minimum grade is',min(subjects_grades, key = subjects_grades.get),' and Maximum grade is',max(subjects_grades, key = subjects_grades.get))





