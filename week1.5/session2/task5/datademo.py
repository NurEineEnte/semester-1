# Week 1.5, Session 2: Task 5
import data
# Write a program here to create a Dataset containing data
# from a file named by the user
filetoread = input("what file would you like to create a dataset from ")
# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
userdata = data.Dataset(filetoread)
print(userdata.data)

print(f"length of dataset: {len(userdata)}")
print(f"mean of dataset: {userdata.mean()}")
print(f"median of dataset: {userdata.median()}")

for i in userdata.data:
    print(i)