class Solution(object):
   
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
                
                

            
    
  