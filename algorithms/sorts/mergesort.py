import time
start_time = time.time()

class Sort(object):

    def insertionSort(this, array):
        sortedArray = []
         
        for i in range(len(array)):
            inserted = False
            #print("inserting: " + str(array[i]))
            for j in range(0, len(sortedArray)):

                if sortedArray[j] > array[i]:
                    sortedArray.insert(j, array[i])
                    inserted = True
                    #print("inserted")
                    #print(sortedArray)
                    break
            if not inserted:
                #print("inserted")
                sortedArray.append(array[i])
                #print(sortedArray)
        #print(sortedArray)
        return sortedArray
   
    def sortArray(this, array):
        if len(array) == 1 or len(array) == 0:
            return array
        elif len(array) == 2:
            if array[0] < array[1]:
                return array 
            else:
                return [array[1] , array[0]]
        else:
            firstHalf = array[:len(array)//2]
            secondHalf = array[len(array)//2:]
            return this.merge( this.sortArray(firstHalf) , this.sortArray(secondHalf))

    def merge(this, array1, array2):
            i = 0
            j = 0
            mergedArray = [];
            for k in range(len(array1) + len(array2)):
                if i < len(array1) and j < len(array2):
                    if array1[i] < array2[j]:
                        mergedArray.append(array1[i])
                        i+=1
                    else:
                        mergedArray.append(array2[j])
                        j+=1
                elif i < len(array1):
                        mergedArray.append(array1[i])
                        i+=1
                elif j < len(array2):
                        mergedArray.append(array2[j])
                        j+=1
                else:
                    return mergedArray
            return mergedArray
                
                

import sys        
sort = Sort()

sortType = sys.argv[1]
array_str = sys.argv[2:]
map_object = map(int, array_str)
array_int = list(map_object)
print("sort type: " + sortType)

if sortType == "merge":
    print(sort.sortArray(array_int))
elif sortType == "insertion":
    print(sort.insertionSort(array_int))
else:
    print("insertion type not found")


print "My program took", time.time() - start_time, "to run"
