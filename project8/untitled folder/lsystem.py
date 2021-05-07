#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 2.0 ##

import sys

class Lsystem:
    def __init__(self, filename=None):
        # assign to the field base, the empty string
        self.base = ''
        self.rules = []
        # if the filename variable is not equal to None
        # call the read method of self with filename as the argument
        
        if filename != None:
            self.read(filename)
    
    def getBase(self):
        return self.base
    
    def setBase(self, b):
        self.base = b
    
    def getRule(self, index):
        return self.rules[index]
    
    def addRule(self,newrule):
        self.rules.append(newrule)
    
    def numRules(self):
        return len(self.rules)
    
    def read( self, filename ):
    # assign to the rules field of self the empty list
        self.rules = []
    # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = open(filename, "r")
    # for each line in fp 
        for line in fp:
        # assign to line the result of calling line.strip()
            line = line.strip()
        # assign to a variable (e.g. words) the result of calling the split() method line
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
        tstring = []
        for c in istring:
            found = False
            for rule in self.rules:
                if rule == c:
                    tstring.append(rule)
                    found = True
                    break
                elif found == False:
                    tstring.append(c)
        return  tstring
    
    def buildString(self, iterations):
        nstring = self.base
        for i in range(iterations):
            nstring = self.replace(nstring)
            
        return nstring

def main(argv):

    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 5

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)
