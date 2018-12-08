# Import dependencies
import pandas as pd
import csv

# Load in data file from resources
poll_data = "Resources/election_data.csv"

# Read and display with pandas
poll_df = pd.read_csv(poll_data)

# Find the total number of votes cast
total_votes = poll_df["Voter ID"].count()

# Display a complete list of candidates who received votes
candidate_list = poll_df["Candidate"].unique()

# The percentage of votes each candidate won -- turning Khan's vote's into readable output
khan_votes = poll_df.loc[poll_df["Candidate"] == "Khan", :]
khan_percentage = (len(khan_votes)/(total_votes))
khan_final = "{:.1%}".format(khan_percentage)

# Correy
correy_votes = poll_df.loc[poll_df["Candidate"] == "Correy", :]
correy_percentage = (len(correy_votes)/(total_votes))
correy_final = "{:.1%}".format(correy_percentage)

# Li
li_votes = poll_df.loc[poll_df["Candidate"] == "Li", :]
li_percentage = (len(li_votes)/(total_votes))
li_final = "{:.1%}".format(li_percentage)

# O'Tooley
otooley_votes = poll_df.loc[poll_df["Candidate"] == "O'Tooley", :]
otooley_percentage = (len(otooley_votes)/(total_votes))
otooley_final = "{:.1%}".format(otooley_percentage)

# The total number of votes each candidate won
vote_counts = poll_df["Candidate"].value_counts()

# Create a list containing election result variables to put into a new dataframe
results_list = {"Khan":2218231, "Correy":704200, "Li":492940, "O'Tooley":105630}

# Create a data frame of the the previous list
df_election = pd.DataFrame()
data = pd.DataFrame({"Vote Totals": results_list})
election_final = df_election.append(data)

# Find the winner of the election based on popular vote.
election_winner = election_final["Vote Totals"].max()
election_winner_final = election_final.loc[election_final["Vote Totals"] == election_winner, :]

# Print election analysis
election_analysis = (print("Election Results"), print("-------------------------"), 
print(f'Total Votes: {total_votes}'), print('-------------------------'), 
print("Khan: " + (khan_final) + ' ({})'.format(len(khan_votes))), 
print("Correy: " + (correy_final) + ' ({})'.format(len(correy_votes))),
print("Li: " + (li_final) + ' ({})'.format(len(li_votes))), 
print("O'Tooley: " + (otooley_final) + ' ({})'.format(len(otooley_votes))), 
print("-------------------------"))
print(f"Winner: " )

# Export to .txt
output = open("output.txt", "w")

line1 = "Election Results"
line2 = "---------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "-------------------------"
line5 = str("Khan: " + (khan_final) + ' ({})'.format(len(khan_votes)))
line6 = str("Correy: " + (correy_final) + ' ({})'.format(len(correy_votes)))
line7 = str("Li: " + (li_final) + ' ({})'.format(len(li_votes)))
line8 = str("O'Tooley: " + (otooley_final) + ' ({})'.format(len(otooley_votes)))
line9 = "-------------------------"
line10 = 
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))