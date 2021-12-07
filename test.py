#task_1
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  

#task_2
def show_student(name ,gpa=0):
    print(name + gpa)

name =(input("Enter your name : "))
gpa=(input("Enter your GPA :"))
show_student(name ,gpa)

#task_3 
subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
key_max = max(subjects_grades,key=subjects_grades.get)
key_min = min(subjects_grades,key=subjects_grades.get)

print('Maximum grade is: ',key_max)
print('Minimum grade is: ',key_min)

    