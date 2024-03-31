import csv

def analyze_votes(filename):
    total_votes = 0
    candidate_votes = {}

    # Reading the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            total_votes += 1
            candidate = row[2] # Assuming candidate name is in the third column (index 2)
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
    
    # Calculating the percentage of votes for each candidate
    percentage_votes = {}
    for candidate, votes_count in candidate_votes.items():
        percentage_votes[candidate] = (votes_count / total_votes) * 100
    
    # Finding the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    return total_votes, candidate_votes, percentage_votes, winner

def main():
    filename = "/Users/lisashimano/Documents/Week 3 Python Challenge/PyPoll/Resources/election_data.csv"
    total_votes, candidate_votes, percentage_votes, winner = analyze_votes(filename)

    print("Total Votes Cast:", total_votes)
    print("Candidates who received votes:", list(candidate_votes.keys()))
    print("\nVote Distribution:")
    for candidate, votes_count in candidate_votes.items():
        print(f"{candidate}: {votes_count} votes ({percentage_votes[candidate]:.3f}%)")
    print("\nWinner of the Election:", winner)

if __name__ == "__main__":
    main()