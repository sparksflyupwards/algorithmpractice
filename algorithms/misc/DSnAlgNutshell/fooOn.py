##testing the O(n) of this function
import math
steps = 0

def Foo(A, start, end):
    start = int(start)
    end = int(end)
    if len(A[start:end]) > 1:
        rangeN = end-start + 1
        chunk = math.floor(rangeN/4)
        Foo(A, start, start + chunk-1)
        Foo(A, start + chunk, start + 2*chunk-1)
        Foo(A, start + 2*chunk, start + 3*chunk-1)
        Foo(A, start + 3*chunk, end)
    else:
        A[0] += 1
        global steps
        steps = steps + 1

    return A
    
import sys      

# if reading from command args
# array_str = sys.argv[2:]
# array_int = map(int, array_str)


inputArray = [i for i in range(10)]
result = Foo(inputArray, 0, len(inputArray)-1)

print(len(inputArray))
print(steps)
print(result)