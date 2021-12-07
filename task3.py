
subjects_grades = {
  'Physics': 91,
  'Math': 82,
  'history': 70,
  'English ': 67
}

maximum = max(subjects_grades, key = subjects_grades.get)
minimum = min(subjects_grades, key = subjects_grades.get)
print("Maximum grade is " + maximum)
print("Minimum grade is " + minimum)