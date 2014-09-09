#!/usr/bin/python
import sys,os

# -------------- Helper functions
# If user neeeds help
def helpText():
    print ""
    print "Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host. "
    print ""
    print "Created by: hansfilipelo & tobyndax"
    print ""
    print "Usage: "
    print "    python suspender.py esxiHostname nrOfSimoultaniousSuspends"
    print ""
    sys.exit

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

            elif sys.argv[i] == "-n":
                nrOflines = int(sys.argv[i+1])

            else:
                    path=sys.argv[i]

if os.path.isfile(path):
    file=open(path)
    stack=list()

    for line in file.readlines():
        stack.append(line)

    for i in range (0,len(stack)):
        print stack.pop()
        if i == nrOflines:
            sys.exit