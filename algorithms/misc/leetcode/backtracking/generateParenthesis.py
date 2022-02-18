
"""
generates all possible valid parenthesis pairs given a parenthesis size n
for example: 
    input: 3
    output: ['((()))', '(()())', '(())()', '()(())', '()()()']
"""

def generateParenthesis( n):
        allParenthesis = []
        def generateParenthesisWorker(n, totalParenthesis, openStack, closeStack):
            if n == 0:
                allParenthesis.append(totalParenthesis)
                return
            possibleOpeners = n - (len(openStack)-len(closeStack))
            
         
            if possibleOpeners < 0:
                return
            if possibleOpeners > 0:
                totalParenthesis+="("
              
                openStack.append("(")
                generateParenthesisWorker(n, totalParenthesis, openStack, closeStack)
                openStack.pop()
                totalParenthesis = totalParenthesis[0:len(totalParenthesis)-1]
            
            if len(openStack) > len(closeStack):
                totalParenthesis+=")"
                closeStack.append(")")
                generateParenthesisWorker(n-1, totalParenthesis, openStack, closeStack)
                closeStack.pop()
                totalParenthesis = totalParenthesis[0:len(totalParenthesis)-1]
        generateParenthesisWorker(n, "", [], [])
        return allParenthesis

import sys
inputValue = sys.argv[1]
try:
    print(generateParenthesis(int(inputValue)))
except:
    print("please enter a valid int")