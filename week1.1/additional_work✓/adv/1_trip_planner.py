"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = int(input("How many miles will you travel? "))
time_hours_input = int(input("How many hours will the journey take? "))
try:
    avg_speed = distance_miles_input / time_hours_input
except:
    print("value cannot be 0")
else:
    if distance_miles_input == 0:
        print("distance cannot be 0")
    elif distance_miles_input < 0 or time_hours_input < 0:
        print("neither value can be negative")
    else:
        print(f"destination is {destination}, and approaching at {avg_speed} mph")

# TODO: convert distance_miles_input and time_hours_input to numbersa
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
