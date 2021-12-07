#TASK1
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

#TASK2
def Show_student(name,GPA=0):
    print(name,GPA)

Show_student("Noarh") #here i dont give a value 
#TASK3
subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
print("Minimum grade is: "+min(subjects_grades ,key =subjects_grades.get))
print("Maximum grade is: "+max(subjects_grades,key=subjects_grades.get))


