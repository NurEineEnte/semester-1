# Worksheet 1.2: Task 1 Solution
try:
    score = int(input("Input a score 0-100 "))
except:
    print("Error: Grade must be an integer between 0 and 100")
    quit()
if score >= 0 and score <= 39:
    grade = "Fail"
elif score >= 40 and score <= 69:
    grade = "Pass"
elif score >= 70 and score <= 100:
    grade = "Distinction"
else:
    print("Error: Grade must be an integer between 0 and 100")
    quit()
print(f"{score} is a {grade}")