def count_divisors(n):
    """Returns the count of divisors of n."""
    count = 0  # Initialize a counter for the divisors
    # Loop through all numbers from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a divisor of n
            count += 1  # Increment the divisor count if it is
    return count  # Return the total count of divisors

def main():
    numbers = []  # List to store the user-input numbers

    # Ask the user how many numbers they want to enter
    while True:
        try:
            size = int(input("How many numbers do you want to enter? "))  # Get the size from user
            if size > 0:
                break  # Exit loop if a valid positive integer is entered
            else:
                print("Please enter a positive integer.")  # Prompt user for correct input
        except ValueError:
            print("Invalid input. Please enter a positive integer.")  # Handle non-integer inputs
    
    # Read numbers from user input
    print(f"Please enter {size} numbers:")
    while len(numbers) < size:  # Continue until we've collected the required number of inputs
        try:
            num = int(input(f"Enter number {len(numbers) + 1}: "))  # Prompt for the next number
            numbers.append(num)  # Add the entered number to the list
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle non-integer inputs
    
    max_divisors = 0  # Variable to track the maximum number of divisors found
    number_with_max_divisors = 0  # Variable to track the number with the maximum divisors
    
    # Find the number with the maximum divisors
    for number in numbers:
        divisor_count = count_divisors(number)  # Count divisors for the current number
        # Update if this number has more divisors or if it's larger with the same divisor count
        if (divisor_count > max_divisors) or (divisor_count == max_divisors and number > number_with_max_divisors):
            max_divisors = divisor_count  # Update maximum divisor count
            number_with_max_divisors = number  # Update the number with the maximum divisors
    
    # Output the result
    print(f"The number with the most divisors is {number_with_max_divisors} with {max_divisors} divisors.")

# Run the main function
if __name__ == "__main__":
    main()  # Start the program
    
