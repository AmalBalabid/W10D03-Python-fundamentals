

# Task1

start = int(input("Enter number start : "))
end = int(input("Enter number end : "))

     
print(start)

print(end)
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)

# Task2
 #  # ------------------------------------------------
def show_student(name,GPA=0):
     print(name,GPA)

show_student("Norah")


   # ------------------------------------------------

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
