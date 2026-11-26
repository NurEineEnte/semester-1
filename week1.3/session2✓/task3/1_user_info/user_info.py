# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
while True:
    name = input("what is your name?")
    age = int(input("how old are you?"))
    favColour = input("what is your favourite colour?")
    with open("user_info.txt", "a") as f:
        f.write(f"{name}\n")
        f.write(f"{age}\n")
        f.write(f"{favColour}\n")
        f.write("\n")
    userprompt = input("do you want to put in more values y/n")
    if userprompt == "n":
        break
