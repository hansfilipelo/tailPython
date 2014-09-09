#!/usr/bin/python
import sys,os

# -------------- Helper functions
# If user neeeds help
def helpText():
    print ""
    print "Simple tail implementation written in python."
    print ""
    print "Created by: hansfilipelo"
    print ""
    print "Usage: "
    print "    python tail.py [-n NR] inFile"
    print ""
    sys.exit(1)

# -------------- main program
if __name__ == "__main__":
    nrOflines=25
    filename=""

    # Check if user needs help
    if len(sys.argv) < 2:
        helpText()

    else:
        for i in range (0,len(sys.argv)):
            if sys.argv[i] == "-h" or sys.argv[i] == "--help":
                helpText()
# ---- Look for arguments
            elif sys.argv[i] == "-n":
                nrOflines = int(sys.argv[i+1])

            else:
                    path=sys.argv[i]
# ---------- Open file
if os.path.isfile(path):
    file=open(path)
    stack=list()

    for line in file.readlines():
        stack.append(line.rstrip('\n'))

stack.reverse()

for i in range (0,len(stack)):
    printString=stack.pop()
    print(printString)
    if i+1 >= nrOflines:
        sys.exit(0)

else:
    print("File " + filename + " does not exist. Please enter a valid file")

