# import os module & CSV
import os
import csv
path = 'C:\\Users\\taiwo\\OneDrive\\Desktop\\phyton-challenge\\PyPoll\\Resources\\election_data.csv'

sum_of_rows=0
x=" "
y=" "
z=" "
# open file with CSV reader
with open (path , 'r') as work2_csv_file:
    csv_reader = csv.reader(work2_csv_file)
    next(csv_reader)
    for row in csv_reader:
        x = str(row[0])
        y = str(row[1])
        z = str(row[2])

        sum_of_rows = sum_of_rows + 1

#Total number of votes
print(sum_of_rows)
#List of candidates
print(set(row[2]))
        


        #print(', '.join(row))
        