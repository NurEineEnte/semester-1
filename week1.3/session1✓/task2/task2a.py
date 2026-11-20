# Week 1.3, Session 1: Task 2a
"""Simple program which demonstrates how an infinite while loop can be prevented, and how they can be fixed,
outputs the powers of 2."""
k = 2
while k <= 200:
    k = 2 * k 
    print(k)

    

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200

# 2. Rewrite the code to directly use the while loop instead of break.