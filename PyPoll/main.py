import csv

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
    i = 0
    canNum = len(candidates)
    voteCount = [0] * canNum
with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for i in range(canNum):
        if row[2] == candidates[i]:
            voteCount[i] += 1

max_votes = max(voteCount)
max_index = voteCount.index(max_votes)
election_winner = candidates[max_index]

print("Election Results")
print("-----------------------------------")
print("Total Votes: "+str(voteTotal))
print(str(election_winner))
print(str(max_votes))