# Aizza Asuncion
# UCBSAN1010Data
# Unit 3 homework - PyBank
# Dr. Spronck
# 5 October 2017

import os
import csv

print('')

# get file path and name
path = input("Enter the file path and/or file name: ")
filename = os.path.join(path)

# initialize variables
total_months = 0
total_revenue = 0
last_month_revenue = 0
total_change_revenue = 0
greatest_increase = 0
greatest_decrease = 0

# open file in read mode and store contents in variable filedata
with open(filename, newline = '') as filedata:
    
    # specify delimiter and store contents in variable
    csvreader = csv.reader(filedata, delimiter = ',')

    # skip header
    next(csvreader, None)

    for row in csvreader:
        # add months
        total_months += 1

        # add total revenue
        total_revenue += int(row[1])

        # calculate change in revenue
        change_in_revenue = int(row[1]) - last_month_revenue
        
        # add change in revenue to total change in revenue
        total_change_revenue += change_in_revenue
        
        # reset last month's revenue
        last_month_revenue = int(row[1])

        # determine greatest increase and greatest decrease in revenue
        if change_in_revenue > greatest_increase:
            greatest_increase = change_in_revenue
            month_greatest_increase = str(row[0])
        elif change_in_revenue < greatest_decrease:
            greatest_decrease = change_in_revenue
            month_greatest_decrease = str(row[0])

# calculate average change in revenue over alll months
average_change_revenue = total_change_revenue / total_months

# print results
print('')
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: "+ str(total_revenue))
print("Average Revenue Change: " + str(int(round(average_change_revenue, 2))))
print("Greatest Increase in Revenue: " + month_greatest_increase + " $" + str(greatest_increase))
print("Greatest Decrease in Revenue: " + month_greatest_decrease + " $" + str(greatest_decrease))

# specify output file to write results to
output_file = 'results.csv'

# open file in write mode and store contents to variable
with open(output_file, 'w', newline='') as resultsfile:

    # specify delimiter in store contents in variable
    csvwriter = csv.writer(resultsfile, delimiter =',')

    # write contents in file
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow([' '])
    csvwriter.writerow(['Total Months:', total_months])
    csvwriter.writerow(['Total Revenue:', total_revenue])
    csvwriter.writerow(['Average Revenue Change:', average_change_revenue])
    csvwriter.writerow(['Greatest Increase in Revenue:', month_greatest_increase, greatest_increase])
    csvwriter.writerow(['Greatest Decrease in Revenue:', month_greatest_decrease, greatest_decrease])