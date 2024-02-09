import csv

employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)



#TO SKIP THE HEADER
next(csv_file)

data = list(csv_file)


print("Highly Effecient Individuals:")
for rec in data:

    name = rec[1]
    age = rec[2]
    salary = rec[3]
    hoursworked = float(rec[4])
    productivity = float(rec[5])

    effeciency = productivity / hoursworked

    if effeciency > 2:
        print(name)

print()
print()

print("Low efficiency individuals:")

for rec in data:

    name = rec[1]
    hoursworked = float(rec[4])
    productivity = float(rec[5])

    effeciency = productivity / hoursworked

    if effeciency < 1:
        print(name)

print()
print()

print("Employees in their 40s:")
i = 0
for rec in data:
    name = rec[1]
    age = float(rec[2])

    if age >= 40:
        print(name)
        i += 1

print()
print(f"Total number of employees in their 40s: {i}")

print()
print()

print("Employees in their 30s:")
i = 0
for rec in data:
    name = rec[1]
    age = float(rec[2])

    if age >= 30 and age < 40:
        print(name)
        i += 1

print()
print(f"Total number of employees in their 30s: {i}")

print()
print()

print("Employees in their 20s:")
i = 0
for rec in data:
    name = rec[1]
    age = float(rec[2])

    if age >= 20 and age < 30:
        print(name)
        i += 1

print()
print(f"Total number of employees in their 20s: {i}")
