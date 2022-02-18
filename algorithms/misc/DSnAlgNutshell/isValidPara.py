
"""
makes a parenthesis input valid by removing necessary characters
for example: 
    input: (2 + 4) * ((34 + 5)
    output: (2 + 4) * (34 + 5)
"""
def makeValid(s):
    paraStack = []
    openStack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == ")":
            paraStack.append({"type":s[i], "idx" : i})
    for i in range(len(paraStack)):
        char = paraStack[i]
        if char["type"] == '(':
            openStack.append(char)
        elif char["type"] == ')':
            if len(openStack) <= 0:
                return makeValid(s[:paraStack[i]["idx"]] + s[paraStack[i]["idx"]+1:])
            else:
                openStack.pop()

    for openPara in openStack:
        s = s[:openPara["idx"]] + s[openPara["idx"] +1 : ]
    return s
    # not len(openStack) > 0

import sys
print(makeValid(sys.argv[1]))
 