import csv

dict = {}
candidates = []
voteTotal = 0
csvPath = "election_data.csv"

with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        voteTotal = voteTotal + 1
        if row[2] not in candidates:
            candidates.append(row[2])
    canNum = len(candidates)
    votes = [canNum]
    for i in range(canNum):
        if row[2] == candidates[i]:
            votes[i] += 1
print("Election Results")
print("-----------------------------------")
print("Total Votes: "+str(voteTotal))
#print(str(voteCount[]))