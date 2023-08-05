def insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j > -1 and l[j] > key:
            l[j+1] = l[j]
            j = j - 1

    return l

result = insertionSort([1, 23, 22, 11, 9, 33, 1, 34, 5, 62])
print(result)

"""
Loop invariant: a loop invariant is a property of a program loop that is true before (and after) each iteration.

Example:
Loop invariate: Subarray l[0,i-1] at the start of each iteration contains the same elements as before the loop's iteration
subarray within the same bounds, but is now in sorted order. 

Initialization: In the first iteration the subarray will consist of just the first element, which is a sorted array.

Maintainance: Informally we can see each iteration will proceed to find the index the new element at i would fit within 
the subarray in order to ensure the subarray is continued to be sorted. This way, we know that each iteration preserves 
the same elements on every iteration and inserts each newly processed key into the position necessary for the subarray 
to be sorted.

Termination: The outer loop terminates when i reaches the value n  (length of l). Placed into the 
loop invariate this means the loop terminates with the subarray l[0, l-1], which is to say the
entire array is guarenteed to be in sorted order and the algorithm is correct 
"""