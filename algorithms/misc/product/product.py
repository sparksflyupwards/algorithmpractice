class Product(object):
    __productType = "basic"
    def __init__(self, productType):
        self.__productType = productType
    
    def operate(self, *args):
        if self.__productType == "basic":
            return self.basic(list(args[0]))

        if self.__productType == "karatsuba":
            return self.karatsuba(list(args[0]))

        else:
            return "Please enter a valid product method"
        

    def basic(self, array):
        total = 1
        for element in array:
            total *= element
        return total

    def whenBreak(self):
        i=0
        while(True):
            if not self.basic([i,i]) == self.karatsuba([i,i]):
                print("WE BROKE HERE"+ i)
                return i
            i = i +1

    def karatsuba(self, array):

        firstHalf = str(array[0])
        secondHalf = str(array[1])
 

        sizeFirstNum = len(firstHalf)
        a = firstHalf[ : len(firstHalf)//2]
        b = firstHalf[len(firstHalf)//2 : ]

        c = secondHalf[ : len(secondHalf)//2]
        d = secondHalf[len(secondHalf)//2 : ]

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)


        if(len(str(a)) > 4):
            highProductNums = [a,c]
            highProduct = self.karatsuba(highProductNums)
            lowProductNums = [b,d]
            lowProduct = self.karatsuba(lowProductNums)
        else:
            highProduct = a  * c
            lowProduct = b * d

        
        sumProduct = a + b
        sumProduct *= c + d
        difference = sumProduct - highProduct - lowProduct
        
        product = highProduct * pow(10,sizeFirstNum) + lowProduct  + difference * pow(10,sizeFirstNum/2)


        print("step: "+firstHalf + " * " + secondHalf + " = " + str(product))
        print("step: "+firstHalf + " * " + secondHalf + " should = " + str(int(firstHalf)*int(secondHalf)))
        return product


import sys      

# if reading from command args
# array_str = sys.argv[2:]
# array_int = map(int, array_str)


product = Product(sys.argv[2])

file_name = sys.argv[1]
f = open(file_name, "r")
array_str = f.read().split()
array_int = map(int, array_str)

print(product.operate(array_int))

#print(product.whenBreak())



