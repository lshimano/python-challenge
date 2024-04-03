# Function to analyze the votes
def analyze_votes(filename):
    total_votes = len(votes):
    candidate_votes = {}

    # Counting the votes for each candidate
    for candidate in votes:
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

def main():
    total_votes, candidate_votes, percentage_votes, winner = analyze_votes

    print("Total Votes Cast:", total_votes)
    print("Candidates who received votes:", list(candidate_votes.keys()))
    print("\nVote Distribution:")
    for candidate, votes_count in candidate_votes.items():
        print(f"{candidate}: {votes_count} votes ({percentage_votes[candidate]:.3f}%)")")
    print("\nWinner of the Election", winner)
    
if __name__ == "__main__":
    main()