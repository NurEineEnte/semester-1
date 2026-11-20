# Week 1.3, Session 1: Task 3b
"""Simple demonstration of looping through a list to remove and show each element, halting when it is empty."""
fruit = ['apple','pear','banana','orange']

while fruit:
	print(fruit.pop())
else:
	print("list is now empty")
# Add an else clause with a message that the list is now empty