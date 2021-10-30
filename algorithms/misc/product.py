class Product(object):
    __productType = "basic"
    def __init__(self, productType):
        self.__productType = productType
        print(self.__productType)
    
    def operate(self, *args):
        if self.__productType == "basic":
            return self.basic(list(args[0]))
        

    def basic(self, array):
        total = 1
        for element in array:
            total *= element
        return total


import sys      
array_str = sys.argv[1:]
array_int = map(int, array_str)

product = Product("basic")
print(product.operate(array_int))

