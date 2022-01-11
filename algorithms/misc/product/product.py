
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
        sizeSecondNum = len(secondHalf)
        zerosAdded = 0
        altered = False

        #   if we have an odd number or the numbers are uneven in length then even them out
        #   and remember divide the answer by the requiste amount and recursively call the function
        #   else just continue with the function

        if sizeFirstNum % 2 != 0 or sizeSecondNum % 2 != 0:
            firstHalf = int(firstHalf) * 10
            secondHalf = int(secondHalf) * 10
            zerosAdded += 2
            altered = True

        if sizeFirstNum > sizeSecondNum:
            sizeDiff = sizeFirstNum - sizeSecondNum
            secondHalf = secondHalf * pow(10, sizeDiff)
            zerosAdded += sizeDiff
            altered =  True

        if sizeFirstNum < sizeSecondNum:
            sizeDiff = sizeSecondNum - sizeFirstNum
            firstHalf = firstHalf * pow(10, sizeDiff)
            zerosAdded += sizeDiff
            altered =  True
       
        
        if altered:
            return self.karatsuba([str(firstHalf), str(secondHalf)]) / pow(10, zerosAdded)

        if not altered:
            a = firstHalf[ : len(firstHalf)//2]
            b = firstHalf[len(firstHalf)//2 : ]

            c = secondHalf[ : len(secondHalf)//2]
            d = secondHalf[len(secondHalf)//2 : ]
            
         
            
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            print("this iteration a b c d")
            print(a)
            print(b)
            print(c)
            print(d)

            if(len(str(firstHalf)) > 4 and len(str(firstHalf))/2%2==0):
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
            product = highProduct * pow(10,sizeFirstNum) + lowProduct  + pow(10,sizeFirstNum / 2) * difference
            product = int(product)

            print("step: "+firstHalf + " * " + secondHalf + " = " + str(product))
            print("cort: "+firstHalf + " * " + secondHalf + " = " + str(int(firstHalf)*int(secondHalf)))

            #   if answers of the karatsuba and the built in multiplcation methods
            #   do not match this message gets printed
            if str(product) != str(int(firstHalf)*int(secondHalf)):
                print("THINGS WENT VERY WRONG HERE\n")
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



