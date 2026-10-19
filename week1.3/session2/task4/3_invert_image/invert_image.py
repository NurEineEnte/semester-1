# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value

with open("invertedimage.pgm","w") as f:
    f.write("P2")
with open("invertedimage.pgm","a") as f:

with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm") as f:
    f.readline()
    f.readline()
    mgv = int(f.readline())
    for line in f:
        line = line.split()
        invertedline = []
        for i in line:
            invertedline.append(mgv - int(i))
        
        

    
# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"