import csv

employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)

#TO SKIP THE HEADER
next(csv_file)

for rec in csv_file:
    total_pay = float(rec[7]) * int(rec[3])
    print(f"Name:   ${rec[1]}")
    print(f"Salary: ${rec[3]}")
    print(f"Bonus:  ${rec[7]}")
    print(f"Pay:    ${total_pay}")
    input()