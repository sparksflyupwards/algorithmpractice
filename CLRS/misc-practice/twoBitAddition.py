import random

twoBitMemo = {}

def addTwoBit(A,B,n):
    if (str(A) + "and" + str(B)) in twoBitMemo:
        return twoBitMemo.get((str(A) + "and" + str(B)))
    C = []
    carry  = 0

    for i in range(n-1, -1, -1):
        
        val = A[i] + B[i] 
        if carry > 0:
            val += 1
            carry -= 1
    
        if val > 1:
            if val % 2 == 0:
                carry = val / 2 + carry
                val = 0 
            else:
                carry = int(val  // 2) + carry
                val = int(val % 2)

        C = [val] + C



   
    while carry > 0:
        C = [1] + C
        carry = carry  - (n - i)

    twoBitMemo[(str(A) + "and" + str(B))] = C
    return C


def getTotal(ans):
    total = 0
    for i in range(len(ans)-1, -1, -1):
        # print(i, ans[i] , pow(2,len(ans)-i))
        total += pow(2,len(ans)-i) * ans[i]
    return total



import concurrent.futures
def checkEqual(A,B):
    ans = addTwoBit(A,B,len(A))
    a = getTotal(A)
    b = getTotal(B)
    total = getTotal(ans)
    return a + b == total


for times in range(1000):
    for size in range(10000):
        A = []
        B = []
        AArray = []
        BArray = []

        for i in range(size):
            A.append(random.randint(0, 1))
            B.append(random.randint(0, 1))
        
        AArray.append(A)
        BArray.append(A)


    with concurrent.futures.ThreadPoolExecutor() as executor:

        future_to_params = {
            executor.submit(checkEqual, array1, array2): (array1, array2)
            for array1, array2 in zip(AArray, BArray)
        }

        
        for future in concurrent.futures.as_completed(future_to_params):
            param = future_to_params[future]
            try:
                result = future.result()
                print(result)
                if not result:
                    raise ValueError("Values not equal! " , param )
                        
            except Exception as exc:
                print(f"Function for {param} generated an exception: {exc}")
            else:
                print(f"Function for {param} completed successfully.")


        