# Week 1.2, Session 2: Task 6
import datetime
try:
    temp = int(input("Please enter the machines temperature in C"))
    pressure = int(input("please enter the machines pressure in psi"))
    operation = int(input("please enter operational status, 1 for operating or 0 for stopped"))
except ValueError:
    print("stinker stonker youre a plonker")
    exit()
if temp >80:
    tempstatus = "machine is smoking hot, shut that stuff off!"
elif 50 <= temp <= 80:
    tempstatus = "machine is doing okay ig thanks for asking, its p fine for now gng"
else:
    tempstatus = "machine doesnt know no nothing bout no ice its just cold yeh you dont need to do nothin"

if pressure > 100:
    pressurestatus = "high pressure please do something yo"
elif 70 < pressure < 100:
    pressurestatus = "its stable or something idk"
else:
    pressurestatus = "pressure is low, great job lad"

if operation == 1:
    if temp > 80 or pressure > 100:
        operationstatus = "its boutta blow shut that sh off"
    else:
        operationstatus = "its going fine king you can relax"
elif operation == 0:
    operationstatus = "machine is stopped, no action needed, maybe u were too lazy to turn it on anyways tho bro"
else:
    operationstatus = "thats not a valid operational state u suck"
    exit()

f = open("machine_log.txt", "a")
f.write(str(temp))
f.write("\n")
f.write(tempstatus)
f.write("\n")
f.write(str(pressure))
f.write("\n")
f.write(pressurestatus)
f.write("\n")
f.write(str(operation))
f.write("\n")
f.write(operationstatus)
f.write("\n")
f.write(str(datetime.datetime.now()))
f.write("\n")
f.close()