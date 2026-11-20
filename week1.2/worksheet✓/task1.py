# Worksheet 1.2: Task 1 Solution
import sys
try:
    score = int(input("Input a score 0-100 "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if score >= 0 and score <= 39:
    grade = "Fail"
elif score >= 40 and score <= 69:
    grade = "Pass"
elif score >= 70 and score <= 100:
    grade = "Distinction"
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")
print(f"{score} is a {grade}")