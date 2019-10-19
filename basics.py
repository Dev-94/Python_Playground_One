import datetime
now = datetime.datetime.now()
print("The date and time is", now)


myNumber = 10
myText = "Hello"

print(myNumber, myText)


x = 10
y = "10"
z = 10.1


sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))


student_grades = [9.1, 9.8, 7.5]
grade_range = list(range(1, 10))
range_step = list(range(1, 10, 3))

print(student_grades)
print(grade_range)
print(range_step)

mySum = sum(student_grades)
length = len(student_grades)
mean = mySum / length
print(mean)

names_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

newSum = sum(names_grades.values())
newLength = len(names_grades)
newMean = newSum / newLength
print(newMean)

keys = names_grades.keys()
print(keys)


monday_temperatures = (1, 4, 5)
print(monday_temperatures)
