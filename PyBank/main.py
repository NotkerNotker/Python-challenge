import csv
import os
import numpy

average = 0
initial = 0
months = 0
net = 0 
change = 0
profits = []
csvPath = "budget_data.csv"

with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    csvreader=list(csv.reader(csvfile))
    initial = (csvreader[0][1])
    for row in csvreader:
        #print(row)
        months = months + 1
        net = net + int(row[1])
        change = int(row[1]) - int(initial)
        profits.append(change)
        initial = row[1]
average = float(numpy.mean(profits))
print("")
print("Financial Analysis")
print("---------------------------------------------")
print("Months: "+str(months))
print("Total: "+str(net))
print("Average Change: "+"{:.2f}".format(average))
print("Greatest Monthly Increase " +str(max(profits)))
print("Greatest Monthly Decrease " +str(min(profits)))
print("")
# print(str(initial))
# print(profits)