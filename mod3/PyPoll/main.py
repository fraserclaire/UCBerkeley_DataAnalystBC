#PyPoll

#need to help with vote counting

import os
import csv
import pandas as pd
from pathlib import Path

#import the dataset
os.chdir("/repos/mygit/UCBerkeley_DataAnalystBC/mod3/PyPoll") 
file = Path("Resources/election_data.csv")
df = pd.read_csv(file, encoding="UTF-8")

df
#>>> df
#        Ballot ID     County                Candidate
#0         1323913  Jefferson  Charles Casper Stockham
#1         1005842  Jefferson  Charles Casper Stockham
#2         1880345  Jefferson  Charles Casper Stockham
#3         1600337  Jefferson  Charles Casper Stockham
#4         1835994  Jefferson  Charles Casper Stockham
#...           ...        ...                      ...
#369706    4714953   Arapahoe     Raymon Anthony Doane
#369707    4497542   Arapahoe     Raymon Anthony Doane
#369708    4085849   Arapahoe     Raymon Anthony Doane
#369709    4592018   Arapahoe     Raymon Anthony Doane
#369710    4660518   Arapahoe     Raymon Anthony Doane

#[369711 rows x 3 columns]

#Calculate the following values:
#1. The total number of votes cast
total_votes = df["Ballot ID"].count()
total_votes

#2. A complete list of candidates who received votes
candidates_wvotes = df["Candidate"].unique()
candidates_wvotes

#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
all_counts = df["Candidate"].value_counts()
charles_counts = df["Candidate"].value_counts()["Charles Casper Stockham"]
diana_counts = df["Candidate"].value_counts()["Diana DeGette"]
raymon_counts = df["Candidate"].value_counts()["Raymon Anthony Doane"]

charles_percent = round((charles_counts / total_votes) * 100 , 3)
diana_percent = round((diana_counts / total_votes) * 100 , 3)
raymon_percent = round((raymon_counts / total_votes) * 100 , 3)

print("Total Votes: " + str(total_votes))
print("Charles Casper Stockham: " + str(charles_percent) + "% (" + str(charles_counts) + ")")
print("Diana DeGette: " + str(diana_percent) + "% (" + str(diana_counts) + ")")
print("Raymon Anthony Doane: " + str(raymon_percent) + "% (" + str(raymon_counts) + ")")

#5. The winner of the election based on popular vote
if diana_percent > charles_percent and diana_percent > raymon_percent:
    print("Winner: Diana DeGette")

if diana_percent < charles_percent and charles_percent > raymon_percent:
    print("Winner: Charles Casper Stockham")

if raymon_percent > charles_percent and diana_percent < raymon_percent:
    print("Winner: Raymon Anthony Doane")

#specify path to write to
out_file = Path("analysis/summary.txt")
with open(out_file, "w") as f:
    f.write("Election Results" + "\n")
    
with open(out_file, "a") as f:
    f.write("-------------------------" + "\n")
    f.write("Total Votes: " + str(total_votes) + "\n")
    f.write("-------------------------" + "\n")
    f.write("Charles Casper Stockham: " + str(charles_percent) + "% (" + str(charles_counts) + ")" + "\n")
    f.write("Diana DeGette: " + str(diana_percent) + "% (" + str(diana_counts) + ")" + "\n")
    f.write("Raymon Anthony Doane: " + str(raymon_percent) + "% (" + str(raymon_counts) + ")" + "\n")
    f.write("-------------------------" + "\n")
    if diana_percent > charles_percent and diana_percent > raymon_percent:
        f.write("Winner: Diana DeGette" + "\n")

    if diana_percent < charles_percent and charles_percent > raymon_percent:
        f.write("Winner: Charles Casper Stockham" + "\n")

    if raymon_percent > charles_percent and diana_percent < raymon_percent:
        f.write("Winner: Raymon Anthony Doane" + "\n")

    f.write("-------------------------" + "\n")