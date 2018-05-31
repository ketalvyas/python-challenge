import os
import csv


file_num = 1


csvpath = os.path.join('election_data_'+ str(file_num) +'.csv')


votes_counted = 0
candidates = {}
candidates_percent_vote = {}
winner = ""
winner_count = 0


with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

  
    for row in csvreader:
        votes_counted += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1


for key, value in candidates.items():
    candidates_percent_vote[key] = round((value/votes_counted) * 100, 2)


for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]


print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(votes_counted))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent_vote[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


file_output = open('election_results_'+ str(file_num) +'.txt','w')


file_output.write("Election Results \n")
file_output.write("------------------------------------- \n\n")
file_output.write("Total Votes: " + str(votes_counted) + "\n")
file_output.write("------------------------------------- \n")
for key, value in candidates.items():
    file_output.write(key + ": " + str(candidates_percent_vote[key]) + "% (" + str(value) + ") \n")
file_output.write("------------------------------------- \n")
file_output.write("Winner: " + winner + "\n")
file_output.write("------------------------------------- \n")