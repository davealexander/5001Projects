#notes


# sys is a system library that gives us access to information from the terminal 
import sys
# print out the sys module variable argb
print(sys.argv) 

#conveer the second command line string to an integer
a = int (sys.argv[1] )
print( a + a) 


def main( argv):
    if len(argv) <2:
        print("usage: python thing.py <argument>")
        exit(-1)

printSomething( argv[1] )
# this code executes when thingpy is imported
if __name__ == "__main__":
    main(sys.argv)
