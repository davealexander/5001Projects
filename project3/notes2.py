wilma = [ 14, 20, 3, 42, "fred" ]
wilma.append( "barney" )
wilma.append( "betty" )
wilma.append( wilma.pop(0) )

print("\nProblem 4 answers")
print(wilma)

wilma.insert( 1, 16 )
wilma.insert( 0, 32 )

print(wilma)

wilma = wilma[:-4]
wilma.sort()

print(wilma)

hmm = [ "willfulness", "soulfulness", "abrasiveness", "adroitness" ]
for word in hmm:    
    root = word[:-4]    
    newword = root + "ly"    
    print(newword)