# Week 1.2, Session 1: Task 3
"""Demonstration of how tuples may be created and used with methods to return data about them, and how they can be unpacked
into variables."""
fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(fruit.index("banana"))

# Display how many times "cherry" occurs
print(fruit.count("cherry"))
# Display how many times "strawberry" occurs
print(fruit.count("strawberry"))
# Unpack tuple into variables
(a,b,c) = fruit
print(a,b,c)