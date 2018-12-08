# Dependencies
import pandas as pd

# Load in data file from resources
bank_data = "Resources/budget_data.csv"

# Read and display with pandas
bank_df = pd.read_csv(bank_data)

# Find the total number of months included in the dataset
total_months = bank_df["Date"].count()

# Find the total net amount of "Profit/Losses" over the entire period
net_end = bank_df["Profit/Losses"].sum()

# Create a new column that displays profit or loss between months
bank_df["Change"] = bank_df["Profit/Losses"].diff()

# Find the average change in "Profit/Losses" between months over the entire period
average_change = bank_df["Change"].mean()

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = bank_df["Change"].max()
greatest_increase_month = bank_df.loc[bank_df["Change"] == greatest_increase, :]

# Find the greatest decrease in losses (date and amount) over the entire period
greatest_decrease = bank_df["Change"].min()
greatest_decrease_month = bank_df.loc[bank_df["Change"] == greatest_decrease, :]

# Print financial analysis
financial_analysis = (print("Financial Analysis"), print("----------------------------"), 
print(f'Total Months: {total_months}'), print(f'Total: {net_end}'), 
print(f'Average Change: ${round(average_change)}'), 
print(f'Greatest Increase in Profits:'), 
print(str(greatest_increase_month)),
print(f'Greatest Decrease in Profits:'), 
print(greatest_decrease_month))

# Export to .txt
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f'Total Months: {total_months}')
line4 = str(f'Total: {net_end}')
line5 = str(f'Average Change: ${average_change}')
line6 = str(f'Greatest Increase in Profits: {greatest_increase_month}')
line7 = str(f'Greatest Decrease in Profits: {greatest_decrease_month}')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))