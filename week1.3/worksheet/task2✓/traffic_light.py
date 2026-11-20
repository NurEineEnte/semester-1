"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Alan
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")
elapsedtime = 0
# Simulate the traffic light system up to time=maxtime in 1-second steps
for systime in range(1, maxtime+1):
    elapsedtime += 1
    if elapsedtime >= 15:
        elapsedtime = 0
    if elapsedtime >= 12:
        state = "amber"
    elif elapsedtime >= 7:
        state = "green"
    elif elapsedtime >= 4:
        state = "red_amber"
    else:
        state = "red"

    print(f"Time {systime:03} State {state}")

# At the end of each step you should output the time and state using the statement on line 14