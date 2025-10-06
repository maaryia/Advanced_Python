from termcolor import colored

def standardize_name(name):
    """Standardizes the name to have the first letter capitalized and the rest lowercase."""
    return name.capitalize()

def main():
    # Read the number of participants
    num_participants = int(input(colored("Enter the number of participants: ","magenta")))
    
    # Initialize lists for male and female participants
    females = []
    males = []

    # Read participant data
    for i in range(num_participants):
        gender = input(f"Participant {i + 1}: What is your gender? (F/M): ").strip().upper()  # Input for gender
        name = input(f"Participant {i + 1}: What is your name? ").strip()  # Input for name
        language = input(f"Participant {i + 1}: What is your language? ").strip()  # Input for language
        
        # Standardize the name
        standardized_name = standardize_name(name)
        
        # Append to the appropriate list based on gender
        if gender == 'F':
            females.append((standardized_name, language))
        elif gender == 'M':
            males.append((standardized_name, language))
        else:
            print("Invalid gender input, please enter 'F' or 'M'.")
    
    # Sort names alphabetically within each gender
    females.sort(key=lambda x: x[0])  # Sort by standardized names
    males.sort(key=lambda x: x[0])    # Sort by standardized names
    
    # Output results
    print(colored("\nFemale Participants:","light_red"))
    for name, language in females:
        print(f"{name} {language}")
    
    print(colored("\nMale Participants:","blue"))
    for name, language in males:
        print(f"{name} {language}")

# Run the program
if __name__ == "__main__":
    main()