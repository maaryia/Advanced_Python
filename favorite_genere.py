from termcolor import colored

def main():
    # List of valid genres
    genres = ["horror", "romance", "comedy", "history", "adventure", "action"]  # Use lowercase for comparison
    
    # Initialize count dictionary
   
    # genre_count = {}  # Initialize an empty dictionary
    # for genre in genres:  # Iterate over each genre in the genres list
    # genre_count[genre] = 0  # Set the initial count for each genre to 0
    
    genre_count = {genre: 0 for genre in genres}

    # Display available genres
    print(colored("Available genres","cyan"))
    for genre in genres:
        print(colored(f"- {genre.capitalize()}", "light_yellow"))  # Display genres in capitalized form

    # Get the number of people with input validation
    while True:
        try:
            num_people = int(input("Enter the number of people: "))
            if num_people <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get each person's information
    for _ in range(num_people):
        name = input("What's your name? ")
        liked_genres = []

        # Prompt for 3 favorite genres
        while len(liked_genres) < 3:
            genre = input(f"{name}, please enter favorite genre number {len(liked_genres) + 1}: ").strip().lower()  # Convert input to lowercase
            # Check if the genre is valid
            if genre in genres and genre not in liked_genres:
                liked_genres.append(genre)
            else:
                print("Invalid genre or already selected. Please choose a valid genre from the list.")

        # Count preferences
        for genre in liked_genres:
            genre_count[genre] += 1

    # Collect results and sort them
    results = sorted(genre_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    print("\nGenre preferences:")
    for genre, count in results:
        print(f"{genre.capitalize()}: {count}")  # Display genres in capitalized form

# Run the program
if __name__ == "__main__":
    main()