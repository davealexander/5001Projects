#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 3.0 ##

import sys
import random

class Lsystem:
    def __init__(self, filename=None):
        # assign to the field base, the empty string
        self.base = ''
        self.rules = {}
        # if the filename variable is not equal to None
        # call the read method of self with filename as the argument
        if filename != None:
            self.read(filename)
    
    #Method that returns base
    def getBase(self):
        return self.base
    #Method that takes self.base and assings whatever the value of b is (str)
    def setBase(self, b):
        self.base = b
    #Method returns the rules in a list 
    def getRule(self, index):
        return self.rules[index]
    #Method that appends a new rule to the rules list
    def addRule(self,newrule):
        self.rules[newrule[0]] = newrule[1:]

    #Method that provides the number of rules inside of the rules list
    def numRules(self):
        return len(self.rules)
    #Method that reads through a text file and determines what is a base and what is a rule
    def read( self, filename ):
    # Var that sets fp to open a filename in system arguments in read mode
        fp = open(filename, "r")
    #Loop that goes through the content of the text file
        for line in fp:
        # var line is set to line.strip which will remove spaces at the beginnning and at the end of a string
            line = line.strip()
        # var words set to line.split that will split the strings by the space value
            words = line.split(' ')
        # if the first item in words is equal to the string 'base'
            if words[0] == 'base':
            # call the setBase method of self with the new base string
                self.setBase(words[1])
        # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
            # call the addRule method of self with the new rule (the slice of words from index 1
                self.addRule(words[1:])
    # call the close method of the file
        fp.close()
    
    def replace(self, istring):
    # assign to a local variable (e.g. tstring) the empty string
        tstring = ''
        for c in istring:
            if c in self.rules:
                tstring = tstring + random.choice(self.rules[c])
            else:
                tstring = tstring + c
        return tstring
    
    #Builds a string based off the rules replacement
    def buildString(self, iterations):
        nstring = self.base
        for i in range(iterations):
            nstring = self.replace(nstring)
        #returns nstring
        return nstring

def main(argv):
    #If length of the argument is less than 2 a usage error will occur and exit the program
    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()
    #sets the filename as system argument position 1
    filename = argv[1]
    #sets the iterations of the build string to 5
    iterations = 5
    #sets the lsystem class to lsys
    lsys = Lsystem()
    #pulls in the lsystem class and read method and takes the argument for filename
    lsys.read( filename )

    #prints lsystem class
    print( lsys )
    #prints the base of lsystem
    print( lsys.getBase() )
    #For loop that iterates over the rules and shows what the base and the replacement will be
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )
    #lstr is assigned the buildstring and the number of iterations it will go through
    lstr = lsys.buildString( iterations )
    #prints the lstring
    print( lstr )
    #returns the main function
    return

if __name__ == "__main__":
    main(sys.argv)
