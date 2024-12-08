lines = []

with open(r'AdventOfCode\2024\Day 2\Test', 'r') as file:
    
    for line in file:
        # Clean up the line, split it, and convert each item to an integer
        line = line.strip()  # Removes trailing newline or extra spaces
        numbers = list(map(int, line.split()))  # Convert the line into a list of integers
        lines.append(numbers)  # Append the list of numbers to the 'lines' list

# Print each line of numbers in the list, one by one
print(lines)