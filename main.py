#Task 1
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))

for i in range(start, end+1):
	if i > 1:
		for j in range(2, i):
			if(i % j == 0):
				break
		else:
			print(i)

#Task 2
def show_student(name,gpa=0):
    print(name,gpa)

show_student("ali","3,15")    
show_student("ali")

#Task 3
subjects_grades = {
  "Physics": 90,
  "Math": 100,
  "history": 70
}
maximum = max(subjects_grades, key = subjects_grades.get)
minimum = min(subjects_grades, key = subjects_grades.get)
print("Maximum grade is " + maximum)
print("Minimum grade is " + minimum)