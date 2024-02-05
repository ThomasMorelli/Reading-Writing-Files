import csv

customers = open('customers.csv','r')
outfile = open('customer_country.csv', 'w')
total_cus = 0

csv_file = csv.reader(customers)

#HEADER
next(csv_file)
outfile.write(f'Full Name, Country\n')


for rec in csv_file:
    outfile.write(f"{rec[1]} {rec[2]}, {rec[4]}\n")
    total_cus += 1
    

outfile.write(f"\nTotal Customers: {total_cus}")

outfile.close()