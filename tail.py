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
    filePaths=[]
    argVector=sys.argv
    argVector.pop(0)

    # Check if user needs help
    if len(sys.argv) < 2:
        helpText()

    else:
        for argument in argVector:
            if argument == "-h " or argument == "--help":
                helpText()
        
        i=int(0)
        for argument in argVector:
            if argument == "-n":
                # Remove "-n" from args
                argVector.pop(i)
                # Get nrOfLines
                nrOflines=int(argVector.pop(i))
                break
            i=i+1

        for argument in argVector:
            filePaths.append(argument)

# ---------- Open file
for path in filePaths:
    if os.path.isfile(path):
        file=open(path)
        stack=list()
        # Read lines from file to stack
        for line in file.readlines():
            stack.append(line.rstrip('\n'))

        # Reverse stack
        stack.reverse()
    
        # Print stack
        for i in range (0,len(stack)):
            printString=stack.pop()
            print(printString)
            # Stop so that we don't print to many lines
            if i+1 >= nrOflines:
                sys.exit(0)
        print ""
    
    # Else file does not exist
    else:
        print ""
        print("File " + path + " does not exist. Please enter a valid file")
        print ""

