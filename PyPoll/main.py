
import os

import csv

print(os.path.join(".",'PyBank_budget_data.csv'))

csvpath = os.path.join('.', 'PyBank_budget_data.csv')

with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

# Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

# Read each row of data after the header

    #print("CSV Data")
    
# Create 2 lists, one to store profit/loss info, another to accumulate monthly change.

    init_list=[]
    diff_list=[]
    
# Intialize other variables

    months = 0
    profit = 0
    avg_change = 0
    abs_change = 0
    best_month = 0
    worst_month = 0
    best_date="x"
    worst_date="y"
    
# print the csv to screen

    for row in csvreader:
               
        row[1] =int(row[1])
        #print(row)
        
# Calculate net profits over the whole time period
        
        profit += row[1]
        #print(profit)
                            
# Calculate the total number of months for which we have data

        months = months + 1
        #print(months)
        
# create a list that stores the profit/loss for each month
        
        init_list.append(row[1])
        #print(init_list)
        
# Conditionals to determine month & magnitude of best profit and worst loss
        
        if row[1] >= int(best_month):
            
            best_month = row[1]
            best_date = row[0]
                         
        elif row[1] < int(worst_month):
                         
            worst_month = row[1]
            worst_date = row[0]
        

#print(months)
#print(profit)
#print(best_month)
#print(worst_month)
#print(best_date)
#print(worst_date)


# Creat Diff_list to calculate the absolute value of monthly change in profit/loss
# So if the first month shows a profit of $200 and second month a loss of $100, the result would be $300 change

diff_list=[] 

    
for j in range(1,len(init_list)):
                   
    diff_list.append(abs(init_list[j] - init_list[j-1]))
              
    #print(diff_list)
    
        
# Compute Average Change (absolute change divided by # months minus one)
    
abs_change = sum(diff_list)
avg_change = int(abs_change/(months - 1))

#print(abs_change)
#print(avg_change)

# Finish report

print("Financial Analysis")
print("----------------------------")
print("#Total Months: " + str(months))
print("$Total: $" + str(profit))
print("#Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + str(best_date) + ", ($" + str(best_month) + ")")
print("Greatest Decrease in Profits: " + str(worst_date) + ", ($" + str(worst_month) + ")")

                          
