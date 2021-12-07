subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }

key_max = max(subjects_grades.keys(), key=(lambda k: subjects_grades[k]))
key_min = min(subjects_grades.keys(), key=(lambda k: subjects_grades[k]))

print('Maximum grade : ',subjects_grades[key_max])
print('Minimum grade : ',subjects_grades[key_min])