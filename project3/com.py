#David Centeno
#5001 Intensive foundations Spring 2021
#2/04/21

import sys

#print(sys.argv)
# we see a list that contains strings

print(sys.argv[0])
a = sys.argv[3]
print(a * 3)
b = int( sys.argv[3] )
print( b * 3)

#The ability to access values in a command line can allow the user of the program to select different outcomes or different values that your program can provide
#In order to use numbers in command line you would need to conver it to an integer. To save the argument you would need to create a variable to save the integer

