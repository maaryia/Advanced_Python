import re

def main():
    # Get user input
    user_text = input("Enter your text: ")
    
    # Use re.sub to replace non-word characters with a space and split into words
    words = re.sub(r'[^\w\s]', ' ', user_text).split()  # Retain spaces for word separation
    
    # Initialize a list to hold key words and their positions
    key_words = []

    # Loop through the words and their positions
    for index, word in enumerate(words, start=1):  # Start indexing from 1
        if word and word[0].isupper():  # Check if the word starts with an uppercase letter
            key_words.append(f"{index}:{word}")  # Add to the list in the required format

    # Output results
    if key_words:
        print("\n".join(key_words))  # Print each key word on a new line
    else:
        print("None")  # No key words found

# Run the program
if __name__ == "__main__":
    main()