###########################################################
 
num1 = int(input("lower number: "))  
num2 = int(input("upper number: "))  
print("Prime numbers between", num1, "and", num2, ": ")

for number in range(num1,num2 + 1):  
   if number > 1:  
       for i in range(2,number):  
           if (number % i) == 0:  
               break
       else:  
           print(number)

############################################################

def Show_student(name,GPA=0):
    print(name,GPA)

Show_student("Tuwaiq")


#############################################################

subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
print("Min grade is: " + min(subjects_grades , key = subjects_grades.get))
print("Max grade is: " + max(subjects_grades , key = subjects_grades.get))