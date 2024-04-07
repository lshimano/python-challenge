import csv

def analyze_financial_data(csv_file):
    total_months = 0
    net_profit_losses = 0
    previous_profit_loss = None
    total_change = 0
    greatest_increase = {"date": None, "amount": float("-inf")}
    greatest_decrease = {"date": None, "amount": float("inf")}
    changes = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Count total number of months
            total_months += 1

            # Calculate net total amount of "Profit/Losses"
            net_profit_losses += int(row["Profit/Losses"])

            # Calculate changes in "Profit/Losses" and update greatest increase/decrease
            current_profit_loss = int(row["Profit/Losses"])
            if previous_profit_loss is not None:
                change = current_profit_loss - previous_profit_loss
                total_change += change
                changes.append(change)
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = row["Date"]
                if change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = row["Date"]
            previous_profit_loss = current_profit_loss

    # Calculate average change
    average_change = total_change / (total_months - 1)

    return {
        "Total Months": total_months,
        "Net Total Amount of Profit/Losses": net_profit_losses,
        "Average Change in Profit/Losses": round(average_change, 2),
        "Greatest Increase in Profits": (greatest_increase["date"], greatest_increase["amount"]),
        "Greatest Decrease in Profits": (greatest_decrease["date"], greatest_decrease["amount"])
    }

def main():
    csv_file = "/Users/lisashimano/Documents/Week 3 Python Challenge/PyBank/Resources/budget_data.csv"
    analysis_results = analyze_financial_data(csv_file)

    # Print analysis results
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
