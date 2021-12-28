friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27},
]

print(friends[0]['name'])

student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

for student in student_attendance:
    print(f'student: {student} attendance: {student_attendance[student]}')

# better way
for student, attendance in student_attendance.items():
    print(f'student: {student} attendance: {attendance}')


# looking for Anne in this dictionarie
if 'Anne' in student_attendance:
    print(f"Anne: {student_attendance['Anne']}")
else:
    print('Anne not exist in this dictionarie')

total_age_friends = 0
# Wants to sum the average of ages
for friend in friends:
    total_age_friends += friend['age']
print(total_age_friends)
print(f'Average {total_age_friends / len(friend)}')
