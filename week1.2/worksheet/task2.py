# Worksheet 1.2: Task 2 Solution
from util import read_numbers
numberlist = read_numbers()


print(f"Minimum = {min(numberlist)}")
print(f"Maximum = {max(numberlist)}")
print(f"Mean = {sum(numberlist) / len(numberlist)}")
numberlist.sort()
if len(numberlist) % 2 == 1:
    median = numberlist[int(len(numberlist)/2)]
else:
    median = (numberlist[len(numberlist)//2] + numberlist[len(numberlist)//2 + 1]) / 2
print(f"Median = {median}")