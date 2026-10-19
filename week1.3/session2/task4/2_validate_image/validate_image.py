# Week 1.3, Session 2: Validate image
# Open a pgm image
# You could handle file errors with try/except
with open("/workspaces/semester-1/week1.3/session2/task4/images/invalid_height.pgm") as f:
    f.readline()
    dimensions = f.readline().split(" ")
    mgv = int(f.readline())
    width = int(dimensions[0])
    height = int(dimensions[1])
    total = 0
    mgvvalid = True
    for lines in f:
        widthtotal = 0
        for pixel in lines.strip().split(" "):
            if pixel != "" and pixel != " " and pixel != "   ":
                widthtotal +=1
                if int(pixel) > mgv or int(pixel) < 0:
                    mgvvalid = False
        total +=1

        
    heightcheck = total
    widthcheck = widthtotal

if height == heightcheck and width == widthcheck and mgvvalid == True:
    print("valid image")
else:
    if height != heightcheck:
        print("invalid height")
    if width != widthcheck:
        print(width, widthcheck)
        print("invalid width")
    if mgvvalid != True:
        print("invalid pixel values")
# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive
# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value