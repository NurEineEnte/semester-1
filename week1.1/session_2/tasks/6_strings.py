# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

#prints original string
print(f"\nOriginal String: {user_string}")
#prints string in lowercase
print(f"Modified String 1: {user_string.lower()}")
#prints string in uppercase
print(f"Modified String 2: {user_string.upper()}")
#prints string and removes all whitespace from the start and end
print(f"Modified String 3: {user_string.strip()}")
#replaces all instances with the letter "a" in the string with "@"
print(f"Modified String 4: {user_string.replace('a', '@')}")
#makes the first letter of the string a capital
print(f"Modified String 5: {user_string.capitalize()}")
#reverses the string
print(f"Modified String 6: {user_string[::-1]}")
#makes the first character of every word in the string a capital
print(f"Modified String 7: {user_string.title()}")
#prints length of the string in no. characters
print(f"Modified String 8: {len(user_string)}")
#prints index of first occurrence of specified char/string
print(f"Modified String 9: {user_string.find('a')}")
#counts number of occurences of specified char/string
print(f"Modified String 10: {user_string.count('a')}")
#checks if the string starts with the specified string
print(f"Modified String 11: {user_string.startswith('Hello')}")
#checks if the string ends with the specified string / characters, a ! in this case
print(f"Modified String 12: {user_string.endswith('!')}")
#checks if the string consists only of alphanumeric characters
print(f"Modified String 13: {user_string.isalnum()}")
#check if the string consists of only alphabetical characters
print(f"Modified String 14: {user_string.isalpha()}")
#check if the string consists of numeric characters
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!