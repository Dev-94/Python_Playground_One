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


monday_temperatures = [8.8, 9.1, 9.9]

print(monday_temperatures)

print("printing mean2 below")


def mean2(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(names_grades)
print(monday_temperatures)
print(mean2(monday_temperatures))
print(type(mean2), type(sum))


if 3 > 1:
    print('a')

print('aa')
print('aaa')


def foo():
    pass
