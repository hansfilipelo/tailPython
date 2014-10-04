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
    if len(sys.argv) < 1:
        helpText()

    else:
        for argument in argVector:
            if argument == "-h " or argument == "--help":
                helpText()
        
        # Look for args
        i=int(0)
        for argument in argVector:
            if argument == "-n":
                # Remove "-n" from args
                argVector.pop(i)
                # Get nrOfLines
                try:
                    nrOflines=int(argVector.pop(i))
                except ValueError:
                    print "Argument -n needs to be followed by a valid number of lines."
                    sys.exit(2)
                break
            i=i+1

        # Get our filenames
        for argument in argVector:
            filePaths.append(argument)

# ---------- Open file
    for path in filePaths:
        if len(filePaths) > 1:
            print (path + " ---------")

        if os.path.isfile(path):
            file=open(path)
            stack=[]
            # Read lines from file to stack
            for line in file.readlines():
                stack.append(line.rstrip('\n'))
            
            stack.reverse()
            output=[]
            
            # Intermediate store
            i=0
            for line in stack:
                output.insert(0,line)
                i=i+1
                # Stop so that we don't print to many lines
                if i+1 > nrOflines:
                    break
            
            for line in output:
                print(line)
            
            sys.exit(0)
            
        # Else file does not exist
        else:
            print ""
            print("File " + path + " does not exist. Please enter a valid file")
            print ""
            sys.exit(3)

sys.exit(0)
