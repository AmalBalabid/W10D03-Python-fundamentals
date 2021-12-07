
def Prime_series(number):
  for iter in range(2,number):
    if is_prime(iter) == True:
      print(iter,end = " ")
    else:
      pass

number = int(input("Enter the input Range : "))
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
Prime_series(number)

def show_student(name, gpa=0):
    print("Student name: "+name)
    if gpa:
        print("GPA: "+gpa)
    else:
        print(0)

show_student("Afnan", "A")
show_student("Afnan")

subject_grades = {'Physics':90, 'Math':100, 'history':70}

maxNum = max(subject_grades, key = subject_grades.get)
print("Maximum grade: ", maxNum)

minNum = min(subject_grades, key = subject_grades.get)
print("Minimum grade: ", minNum)


