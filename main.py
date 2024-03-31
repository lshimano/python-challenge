import csv

def analyze_records(csv_file):
    total_months = 0
    net_profit_losses = 0
    previous_profit_loss = None
    total_change = 0
    greatest_increase = {"date": None, "amount": float("-inf")}
    greatest_decrease = {"date": None, "amount": float("inf")}

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Counting total months
            total_months += 1

            # Calculating net total amount of "Profit/Losses"
            net_profit_losses += int(row["Profit/Losses"])

            # Calculating changes in "Profit/Losses" and updating greatest increase/decrease
            if previous_profit_loss is not None:
                change = int(row["Profit/Losses"]) - previous_profit_loss
                total_change += change
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = row["Date"]
                if change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = row["Date"]
            previous_profit_loss = int(row["Profit/Losses"])

    # Calculating average change
    average_change = total_change / (total_months - 1)

    return {
        "Total number of months": total_months,
        "Net total amount of Profit/Losses": net_profit_losses,
        "Average of changes in Profit/Losses": round(average_change, 2),
        "Greatest increase in profits": (greatest_increase["date"], greatest_increase["amount"]),
        "Greatest decrease in profits": (greatest_decrease["date"], greatest_decrease["amount"])
    }

def write_results_to_file(results, output_directory):
    output_file = os.path.join(output_directory, "analysis_results.txt")
    with open(output_file, 'w') as file:
        for key, value in results.items():
            if key.startswith("Greatest"):
                file.write(f"{key}: {value[0]} (${value[1]})\n")
            else:
                file.write(f"{key}: {value}\n")

import os

def main():
    csv_file = "/Users/lisashimano/Documents/Week 3 Python Challenge/PyBank/Resources/budget_data.csv"
    output_directory = "/Users/lisashimano/Documents/Week 3 Python Challenge/PyBank"
    analysis_results = analyze_records(csv_file)
    write_results_to_file(analysis_results, output_directory)
    print(f"Analysis results have been written to {os.path.join(output_directory, 'analysis_results.txt')}")

if __name__ == "__main__":
    main()

