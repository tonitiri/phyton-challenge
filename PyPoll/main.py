# import os module & CSV
import os
import csv
path = 'C:\\Users\\taiwo\\OneDrive\\Desktop\\Working\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv'
 
# open file with CSV reader
with open (path , 'r') as work2_csv_file:
    csv_reader = csv.reader(work2_csv_file)
    next(csv_reader)
    for row in csv_reader:
        #print(', '.join(row)).headers
        #print(row[0])