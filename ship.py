def findMissingParts(str):
    keys = ["B","F","T","L","C"]
    found = [0,0,0,0,0]
    
    for i in range(len(str)):
        for j in range(len(keys)):
            if str[i].upper()==keys[j].upper():
                found[j]=1;
    
    unfound = [];
    
    for i in range(len(found)):
        if not found[i]:
            unfound.append(i)
    
    answerString = ""
    
    for i in range(len(unfound)):
        answerString = answerString + keys[unfound[i]]
    return answerString

import sys
in_val = str(sys.stdin.readline())
print(findMissingParts(in_val))


