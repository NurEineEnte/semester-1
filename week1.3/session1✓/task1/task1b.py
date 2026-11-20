# Week 1.3, Session 1: Task 1b
"""Program begins with a full list of fruit, outputs them one by one as it removes them from the list."""
fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?

#pop removes the  first item out of a list and also returns it
# What features of Python does it rely on?
#list methods