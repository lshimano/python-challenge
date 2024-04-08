import csv

def analyze_votes(filename):
    total_votes = 0
    candidate_votes = {}

    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            total_votes += 1
            candidate = row[2] # Assuming candidate name is in the third column
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
    
    # Calculate the percentage of votes for each candidate
    percentage_votes = {}
    for candidate, votes_count in candidate_votes.items():
        percentage_votes[candidate] = (votes_count / total_votes) * 100
    
    # Find the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    return total_votes, candidate_votes, percentage_votes, winner

def save_analysis_to_txt(total_votes, candidate_votes, percentage_votes, winner):
    with open('election_results.txt', 'w') as file:
        file.write("Election Results\n\n")
        file.write(f"Total Votes: {total_votes}\n\n")
        for candidate, votes_count in candidate_votes.items():
            file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes_count})\n")
        file.write(f"\nWinner: {winner}\n")

def main():
    filename = 'election_data.csv'
    total_votes, candidate_votes, percentage_votes, winner = analyze_votes(filename)
    save_analysis_to_txt(total_votes, candidate_votes, percentage_votes, winner)
    print("Analysis saved to election_results.txt")

if __name__ == "__main__":
    main()