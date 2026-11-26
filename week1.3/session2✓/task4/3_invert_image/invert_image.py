# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
f = open("invertedimage.pgm","w")
f.close()


with open("../images/feep.pgm","r") as f:
    f.readline()
    dimensions = f.readline()
    mgv = int(f.readline())
    with open("invertedimage.pgm","a") as g:
        g.write("P2\n")
        g.write(f"{dimensions}")
        g.write(f"{mgv}\n")
    for line in f:
        line = line.split()
        invertedline = ""
        invertedline += str(mgv - int(line[0]))      
        for i in line[1:]:
            invertedval = str(mgv - int(i))
            invertedline += " "
            spacestoadd = len(str(mgv)) - len(str(invertedval))
            for g in range(spacestoadd):
                invertedline += " "
            invertedline += invertedval
            
        invertedline += "\n"
        with open("invertedimage.pgm","a") as g:
            g.write(invertedline)
    

        
        

    
# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"