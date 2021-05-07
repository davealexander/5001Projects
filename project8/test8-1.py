# Bruce Maxwell
# spring 2013
# lsystem version 2 test function

import lsystem 
import sys

# test function that creates an Lsystem from a file and prints out its
# contents
def main( argv ):
    """
    Tests the Lsystem class.
    This program creates an Lsystem object from a file and prints
    out the contents. It expects the name of an L-system file
    as input on the command line.
    """

    if len(argv) < 2: 
        print( 'usage: python lsystem.py <lsystem filename>' )
        exit()

    # test an existing lsystem
    ls = lsystem.Lsystem( argv[1] )

    print( 'Case 1', argv[1] )
    print( ls.getBase() )
    
    rule = ls.getRule( 0 )
    print( rule[0] + ' -> ' + rule[1] )

    # create a new lsystem from scratch
    ns = lsystem.Lsystem()

    ns.setBase( 'F--F--F' )
    ns.addRule( [ 'F', 'F+F--F+F'] )

    print( '\nCase 2' )
    print( ns.getBase() )
    
    rule = ns.getRule( 0 )
    print( rule[0] + ' -> ' + rule[1] )
    

if __name__ == '__main__':
    main( sys.argv )
