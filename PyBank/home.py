import os
import csv

filepath = os.path.join("Resources","budget_data.csv")

with open(filepath) as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data)
    count = 0
    sum = 0
    net_change = []
    previous_row=0
    current_row=0
    sum_change=0
    
    

    for row in csv_data:
        count = count + 1
        sum = int(row[1])+sum

        current_row=int(row[1])
        (current_row-previous_row)

        
        net_change.append(current_row-previous_row)
        

        previous_row=current_row

    
    net_change = net_change[1:]
    sum1 = 0
    greatest_current_loss=0
    greatest_current_gain=0
    
    for x in net_change:
        sum1 += x

        if x < 0:
            if x < greatest_current_loss:
                greatest_current_loss = x 
        if x > 0:
            if x > greatest_current_gain:
                greatest_current_gain = x

        # print(greatest_current_loss)

    

    print('Financial Analysis')  
print('----------------------------')       
#Net Total Profit
print("Net Total Profit: $",sum) 
#Total number of months
print("Total number of months: ",count)
#Average Profit
print("Average Profit: $",(sum/count))
print("Average Change: $",sum1/len(net_change))
# print("Greatest Increase in Profits: $",greatest_current_gain)
# print("Greatest Decrease in Profits: $",greatest_current_loss)