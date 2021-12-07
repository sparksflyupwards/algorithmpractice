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

        highProduct = a  * c
        lowProduct = b * d
        sumProduct = a + b
        sumProduct *= c + d
        difference = sumProduct - highProduct - lowProduct
        
        product = highProduct * pow(10,sizeFirstNum) + lowProduct  + difference * pow(10,sizeFirstNum/2)



        print(a)
        print(b)

        print(c)
        print(d)

        print(highProduct)
        print(lowProduct)
        print(sumProduct)
        print(difference)
        print("product: " + str(product))
        print("karatsuba")
        return 9


import sys      

# if reading from command args
# array_str = sys.argv[2:]
# array_int = map(int, array_str)


product = Product(sys.argv[2])

file_name = sys.argv[1]
f = open(file_name, "r")
array_str = f.read().split()
print(array_str)
array_int = map(int, array_str)

print(product.operate(array_int))



