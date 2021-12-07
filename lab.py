# Task 1 : 
# print("Task 1 :  Display all prime numbers within a range")
# from_range = int(input("From :"))
# to_range = int(input("To :"))

# def check_is_prime(x):
#     flag = True
    
#     for i in range(2,x):
#         if x % i == 0:
#             flag = False
            
#     return flag

# for i in range(from_range,to_range+1):
#     if check_is_prime(i):
#         print(i)


# Task 2 :

# def show_student(name, gpa=0):
    
#     print (name ," Has " ,gpa  )

# show_student("saad",3.25)


# Task 3 :


subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }




def find_max_and_min(s_g):
    max_number = max(s_g.values())
    min_number = min(s_g.values())
    for name, grade in s_g.items():
        if grade == max_number:
            print("Max is " , name)
        if  grade == min_number:
            print("Min is " , name)





find_max_and_min(subjects_grades)