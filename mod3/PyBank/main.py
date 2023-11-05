#Module 3 Challenge - Python

#create new folder in repo called "mod3"

########
#Pybank
#dataset has Date and Profit/Losses data

import os
import csv
import pandas as pd
from pathlib import Path

#import the dataset
os.chdir("/repos/mygit/UCBerkeley_DataAnalystBC/mod3/PyBank") 
file = Path("Resources/budget_data.csv")
df = pd.read_csv(file, encoding="UTF-8")

df
#>>> df
#      Date  Profit/Losses
#0   Jan-10        1088983
#1   Feb-10        -354534
#2   Mar-10         276622
#3   Apr-10        -728133
#4   May-10         852993
#..     ...            ...
#81  Oct-16        -729004
#82  Nov-16        -112209
#83  Dec-16         516313
#84  Jan-17         607208
#85  Feb-17         382539

#[86 rows x 2 columns]

#Calculate the following values:
#1. total number of months included in the dataset
total_months = df["Date"].count()
total_months

#2. net total amount of "Profit/Losses" over the entire period
net_total = df["Profit/Losses"].sum()
net_total

#3. changes in Profit/Losses over the entire period
df["difference"] = 0 #add column to save differences
new_df = pd.DataFrame(df) #set as dataframe

prev_total = new_df["Profit/Losses"].iloc[0] #set first total value

for i in range(86):
    new_df["difference"].iloc[i] = new_df["Profit/Losses"].iloc[i] - prev_total
    prev_total = new_df["Profit/Losses"].iloc[i]


new_df[75:86]
diff_df = new_df["difference"][1:86]
#average of those changes
average_change = round(diff_df.mean(), 2) #round the average change to a number with 2 decimal points
average_change

#4. greatest increase in profits (date and amount) over the entire period
max_inc = new_df["difference"].max()
max_inc
max_index = new_df["difference"].loc[new_df["difference"] == max_inc].index
max_date = new_df["Date"].iloc[max_index]
max_date_ext = max_date.iloc[0]

#5. greatest decrease in profits (date and amount) over the entire period
max_dec = new_df["difference"].min()
max_dec
min_index = new_df["difference"].loc[new_df["difference"] == max_dec].index
min_date = new_df["Date"].iloc[min_index]
min_date_ext = min_date.iloc[0]

print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_date_ext) + " ($" + str(max_inc) + ")")
print("Greatest Decrease in Profits: " + str(min_date_ext) + " ($" + str(max_dec) + ")")

#specify path to write to
out_file = Path("analysis/summary.txt")
with open(out_file, "w") as f:
    f.write("Financial Analysis" + "\n")
    
with open(out_file, "a") as f:
    f.write("----------------------------" + "\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total: $" + str(net_total) + "\n")
    f.write("Average Change: $" + str(average_change) + "\n")
    f.write("Greatest Increase in Profits: " + str(max_date_ext) + " ($" + str(max_inc) + ")" + "\n")
    f.write("Greatest Decrease in Profits: " + str(min_date_ext) + " ($" + str(max_dec) + ")" + "\n")