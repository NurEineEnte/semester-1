# Week 1.3, Session 1: Task 5a
"""creates a list data structure of the characters from the course string, sorts the list into alphabetical order"""
course = "computer science"
mylist = []
for i in range(len(course)):
	mylist.append(course[i])
print(mylist)
mylist.sort()
print(mylist)


