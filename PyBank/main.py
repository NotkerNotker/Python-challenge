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
    #take out header
    csv_header = next(csvfile)
    csvreader=list(csv.reader(csvfile))
    initial = (csvreader[0][1])
    for row in csvreader:
        months = months + 1
        net = net + int(row[1])
        #calculate each difference in profits and add value to list
        change = int(row[1]) - int(initial)
        profits.append(change)
        initial = row[1]
#calculate average of changes
average = (numpy.mean(profits))

print("")
print("Financial Analysis")
print("---------------------------------------------")
print("Months: "+str(months))
print("Total: "+str(net))
print("Average Change: "+"{:.2f}".format(average))
print("Greatest Monthly Increase " +str(max(profits)))
print("Greatest Monthly Decrease " +str(min(profits)))
print("")

with open("Output.txt", "w") as file:
    file.write("\n")
    file.write("Financial Analysis \n")
    file.write("--------------------------------------------- \n")
    file.write("Months: "+str(months)+"\n")
    file.write("Total: "+str(net)+"\n")
    file.write("Average Change: "+"{:.2f}".format(average)+"\n")
    file.write("Greatest Monthly Increase " +str(max(profits))+"\n")
    file.write("Greatest Monthly Decrease " +str(min(profits))+"\n")
    file.write("\n")