import csv
import os
import pathlib

# print(pathlib.Path(__file__).parent.resolve())

csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "election_data.csv")

total_votes = 0 
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
max_votes = 0
winner = ""

# # Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    # rows = csv.reader()

    for row in csv_reader:
        # print(row)
        # total_votes = total_votes + 1
        total_votes += 1        

        if row[2] == "Khan":                # Adding all the votes from each candidate 
            Khan_votes += 1                 # Khan_votes = Khan_votes + 1
        elif row[2] == "Correy":
            Correy_votes += 1   
        elif row[2] == "Li":
            Li_votes += 1 
        elif row[2] == "OTooley":
            OTooley_votes += 1 

    candidates_dict = {"Khan": Khan_votes,      # Created a Dictionary to 
                "Correy": Correy_votes,
                "Li": Li_votes,
                "OTooley":  OTooley_votes
                }

    for candidate, votes in candidates_dict.items(): 
        if votes > max_votes:
            max_votes = votes
            winner = candidate

        # exit()
# print(Khan_votes)
# print(total_votes)
# print()

output = f"""                                                                                   
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {(Khan_votes / total_votes) * 100:.3f}% ({Khan_votes})
Correy: {(Correy_votes / total_votes) * 100:.3f}% ({Correy_votes})
Li: {(Li_votes / total_votes) * 100:.3f}% ({Li_votes})
O'Tooley: {(OTooley_votes / total_votes) * 100:.3f}% ({OTooley_votes})
-------------------------
Winner: {winner}
-------------------------
"""                                                                     # f string to print all the data needed.

print(output)

with open("PyPoll/Analysis/pyPoll_output.csv", 'w') as outputFile:                 # create the file in seperate folder
    outputFile.write(output)