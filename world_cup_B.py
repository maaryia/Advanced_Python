# def main():
#     # List of team names
#     team_names = ["Iran", "Portugal", "Spain", "Morocco"]

#     # Initialize a dictionary to hold statistics for each team
#     teams = {team: {"wins": 0, "losses": 0, "draws": 0, "goals_for": 0, "goals_against": 0, "points": 0} for team in team_names}

#     # Dictionary to hold match results
#     results = {
#         ("Iran", "Spain"): "2-2",
#         ("Iran", "Portugal"): "2-1",
#         ("Iran", "Morocco"): "1-2",
#         ("Spain", "Portugal"): "2-2",
#         ("Spain", "Morocco"): "3-1",
#         ("Portugal", "Morocco"): "2-1",
#     }

#     # Process each match in the results dictionary
#     for (left_team, right_team), result in results.items():
#         score_left, score_right = map(int, result.split('-'))  # Split the result into scores
        
#         # Update goals for both teams
#         teams[left_team]["goals_for"] += score_left
#         teams[left_team]["goals_against"] += score_right
#         teams[right_team]["goals_for"] += score_right
#         teams[right_team]["goals_against"] += score_left

#         # Determine the match outcome and update statistics
#         if score_left > score_right:  # Left team wins
#             teams[left_team]["wins"] += 1
#             teams[right_team]["losses"] += 1
#             teams[left_team]["points"] += 3
#         elif score_left < score_right:  # Right team wins
#             teams[right_team]["wins"] += 1
#             teams[left_team]["losses"] += 1
#             teams[right_team]["points"] += 3
#         else:  # Draw
#             teams[left_team]["draws"] += 1
#             teams[right_team]["draws"] += 1
#             teams[left_team]["points"] += 1
#             teams[right_team]["points"] += 1

#     # Calculate goal difference for each team
#     for team in teams.values():
#         team["goal_difference"] = team["goals_for"] - team["goals_against"]

#     # Sort teams based on points, wins, and alphabetical order
#     sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["points"], -x[1]["wins"], x[0]))

#     # Output the results in the specified format
#     for team_name, stats in sorted_teams:
#         print(f"{team_name} wins:{stats['wins']} , loses:{stats['losses']} , draws:{stats['draws']} , "
#               f"goal difference:{stats['goal_difference']} , points:{stats['points']}")

# # Run the main function
# if __name__ == "__main__":
#     main()



def initialize_teams():
    """Initialize the teams' statistics."""
    team_names = ["Iran", "Portugal", "Spain", "Morocco"]
    return {team: {"wins": 0, "losses": 0, "draws": 0, "goals_for": 0, "goals_against": 0, "points": 0} for team in team_names}

def update_statistics(teams, left_team, right_team, score_left, score_right):
    """Update team statistics based on match results."""
    # Update goals for both teams
    teams[left_team]["goals_for"] += score_left
    teams[left_team]["goals_against"] += score_right
    teams[right_team]["goals_for"] += score_right
    teams[right_team]["goals_against"] += score_left

    # Determine the match outcome and update statistics
    if score_left > score_right:  # Left team wins
        teams[left_team]["wins"] += 1
        teams[right_team]["losses"] += 1
        teams[left_team]["points"] += 3
    elif score_left < score_right:  # Right team wins
        teams[right_team]["wins"] += 1
        teams[left_team]["losses"] += 1
        teams[right_team]["points"] += 3
    else:  # Draw
        teams[left_team]["draws"] += 1
        teams[right_team]["draws"] += 1
        teams[left_team]["points"] += 1
        teams[right_team]["points"] += 1

def main():
    # Initialize teams
    teams = initialize_teams()
    
    # Predefined matches
    matches = [
        ("Iran", "Spain"),
        ("Iran", "Portugal"),
        ("Iran", "Morocco"),
        ("Spain", "Portugal"),
        ("Spain", "Morocco"),
        ("Portugal", "Morocco"),
    ]

    # Process user input for each match
    for match in matches:
        # Get match result from the user
        result_input = input(f"Enter result for {match[0]} vs {match[1]} (format X-Y): ")
        score_left, score_right = map(int, result_input.split('-'))  # Split the result into scores

        # Update statistics based on user input
        update_statistics(teams, match[0], match[1], score_left, score_right)

    # Calculate goal difference for each team
    for team in teams.values():
        team["goal_difference"] = team["goals_for"] - team["goals_against"]

    # Sort teams based on points, wins, and alphabetical order
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["points"], -x[1]["wins"], x[0]))

    # Output the results in the specified format
    for team_name, stats in sorted_teams:
        print(f"{team_name} wins:{stats['wins']} , loses:{stats['losses']} , draws:{stats['draws']} , "
              f"goal difference:{stats['goal_difference']} , points:{stats['points']}")

# Run the main function
if __name__ == "__main__":
    main()