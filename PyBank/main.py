# import os module & CSV
import os
import csv
path = 'C:\\Users\\taiwo\\OneDrive\\Desktop\\phyton-challenge\\PyBank\\Resources\\budget_data.csv'
 
# open file with CSV reader
with open (path , 'r') as work1_csv_file:
    csv_reader = csv.reader(work1_csv_file)
    next(csv_reader)
    for row in csv_reader:
        #print(', '.join(row))
        print(row[0])

        #assigning variable type to columns
        months = str(row[0])
        profit_loss = float(row[1])

        #total number of months
        #print(months).value_count()
        # Net total profit/losses
        #print(len('months'))
        print(profit_loss).value_count

    # def average(numbers):
    # length = len(numbers)
    # total = 0.0
    # for number in numbers:
    #     total += number
    # return total / length
          

        

