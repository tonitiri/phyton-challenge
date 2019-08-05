# import os module & CSV
import os
import csv
path = 'C:\\Users\\taiwo\\OneDrive\\Desktop\\phyton-challenge\\PyBank\\Resources\\budget_data.csv'

net_profit=0
sum_rows=0
average=0
greatest_increase=0
budget_data=0

# open file with CSV reader
with open (path , 'r') as work1_csv_file:
    csv_reader = csv.reader(work1_csv_file)
    next(csv_reader)


#     for row in csv_reader:
    
#          x = int(row[1])

#          net_profit = x + net_profit
#          sum_rows = sum_rows + 1
#          average = net_profit/sum_rows
        
         
         
# #Net Total Profit
# print(net_profit) 
# #Total number of months
# print(sum_rows)
# #Average
# print(average)

    for row in csv_reader:
        #print(row)
        #print(row[0])
        print(range(row[1]))



    


    #     #print(', '.join(row))
    #     #print(row[1])
    #     total_rows = total_rows + 1

    #     #1. Total Number of Months
    #     print(total_rows)

        # budget_data_list.extend([row[1]])
        # budget_data_list.extend([x])
    #     print(type(budget_data_list))
    #     # print(type(x))

#for n in range(x)
    
        
        






        

        
          

        

