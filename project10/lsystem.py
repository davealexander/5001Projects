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
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            # elif the character is )
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            # elif we are in number-parsing-mode
            elif pargrab:
                # add this character to the number string
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute( replacement, parval )
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod( replacement, parstring, c )
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring
    
    def substitute(self, sequence, value ):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:

            # parameter expression starts
            if c == '(':
                # set the state variable to True (grabbing the expression)
                exprgrab = True
                expr = ''
                continue

            # parameter expression ends
            elif c == ')':
                exprgrab = False
                # create a function out of the expression
                lambdafunc = eval( 'lambda x: ' + expr )
                # execute the function and put the result in a (string)
                newpar = '(' + str( lambdafunc( value ) ) + ')'
                outsequence += newpar

            # grabbing an expression
            elif exprgrab:
                expr += c

            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c 

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol 
            inserts the parameter, with parentheses, 
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                # add the parameter string in parentheses
                tstring += '(' + modstring + ')'
            tstring += c
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
