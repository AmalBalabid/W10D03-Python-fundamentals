  
for num in range(50,100 + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  


def show_student(name,GPA="0"):
  print("name: "+name+" GPA: "+GPA)

show_student("shahad","4.4")

show_student("shahad")

subjects_grades = { "Physics": 90, "Math": 100, "history": 70 }
key_max = max(subjects_grades,key= subjects_grades.get)
key_min = min(subjects_grades,key= subjects_grades.get)

print("Minimum grade is",key_min,"Maximum grade is",key_max)