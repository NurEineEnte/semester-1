import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
print(random.choice([k for k in range(3,21,2)]))
# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
