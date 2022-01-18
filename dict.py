# this is a list
temperatures = [ 9.4, 8.8, 7.7]

# this is a dictionary with its value as tuples
day_temperatures = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}

# this is a basic dictionary
student_grades = { "Mary": 10.1, "Kiran": 10.3}

mysum = sum(student_grades.values())
length = len(student_grades)
mean  = mysum / length
print(day_temperatures['evening'])
print("Result: ", mean)