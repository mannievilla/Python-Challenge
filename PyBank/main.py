# from logging.config import valid_ident
# from operator import index
import os
import csv
import pathlib

# Set path for file
csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "budget_data.csv")



# total_months = 0
# total = 0
# average_change = 0
# greatest_increase = 0
# greatest_decrease = 0
# max = 0


# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    data = list(csv_reader)
    # data = (list(csv.reader(csvfile)))
    # #data = iter(list(csv.reader(csvfile, delimiter=",")))
    # #next(data)
    # data = data[1:]
    # total_months = len(data)
    # header = next(csv_reader) 
    # maxnum = max(csv_reader, key=lambda row: int(row[1]))
    # print(maxnum)
    # next(csv_reader)   ## remove tag after you remove maxnum tryout and  add header = 
    column_pl = [] 
    column_dates = []
    column_change = []

    profit_loss = 0

    for row in data[1:]:
        column_dates.append(row[0])
        column_pl.append(int(row[1]))
        # greatest_increase = int(row[1])
        # print(greatest_increase)
        # print(row[1])
        # column_pl = (row[1])
        # total_months += 1
        column_change.append(int(row[1])-profit_loss)
        profit_loss = int(row[1])
        # print(total_months)
        total_months = len(column_dates)
        # total += int(row[1]) 
        total = sum(column_pl)
        # average = total / total_months
        # print(average)
        average = sum(column_change[1:]) / total_months
        # average = total / total_months
        print(average)
        greatest_increase = max(column_change)
        index = column_change.index(greatest_increase)
        increase_date = column_dates[index]
                                            # if max < int(row[1]):
                                            #max = int(row[1])
        greatest_decrease = min(column_change)
        index = column_change.index(greatest_decrease)
        decrease_date = column_dates[index] 
        # maxdiff = max - int(row[1])     # print(max)
        # print(maxdiff)
        # greatest_increase = int(row[1])
        # maxnum = max(greatest_increase)
        # print(maxnum)
        # print(total)
        # for x in greatest_increase:
        #         if x > max:
        #             max = x  
        # print(max)
output = f"""
   Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average  Change: ${average :.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

print(output)

with open("PyBank/Analysis/pyBank_output.csv", 'w') as outputFile:                 # create the file in seperate folder
    outputFile.write(output)
    #