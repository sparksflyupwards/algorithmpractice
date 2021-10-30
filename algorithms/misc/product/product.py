class Product(object):
    __productType = "basic"
    def __init__(self, productType):
        self.__productType = productType
    
    def operate(self, *args):
        if self.__productType == "basic":
            return self.basic(list(args[0]))
        else:
            return "Please enter a valid product method"
        

    def basic(self, array):
        total = 1
        for element in array:
            total *= element
        return total


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



