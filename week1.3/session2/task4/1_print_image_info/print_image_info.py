# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm") as f:
    f.readline()
    dimensions = f.readline().split(" ")
    mgv = f.readline()
    width = dimensions[0]
    height = dimensions[1]

print(f"Dimensions: {width} x {height}")
print(f"Max Gray Value: {mgv}")

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)