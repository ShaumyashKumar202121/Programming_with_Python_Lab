#Lab-9: Design an abstract class for the Sorting methods that 
#will force the inherited class to include all the relevant components 
#like sort(), display(), etc
from abc import ABC , abstractmethod #declaring abstract method
class sorting(ABC):
    @abstractmethod
    def display(self): # abstract method display()
        pass
    
    @abstractmethod
    def sort(self):  # abstract method sort()
        pass

class insertionSort(sorting):
    def sort(self,array):
        n = len(array)
        for i in range(1,n):
            key = array[i]
            j = i - 1
            while array[j] > key and j >= 0:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
            
    def display(self,array):
        print(array)
    
class selectionSort(sorting):
    def sort(self,array):
        n = len(array)
        for i in range(0,n-1):
            index_of_min = i
            for j in range(i+1,n):
                if  array[j] < array[index_of_min] :
                    index_of_min = j
            array[i],array[index_of_min] = array[index_of_min],array[i]
    
    def display(self,array):
        print(array)

# Driver code
arr = [6,7,45,76,67,1,89,18,0]
print("The Array is"); 
print(' '.join(map(str, arr)))
print("after insertion sort it is")
ins = insertionSort()
ins.sort(arr)
ins.display(arr)
print("after selection sort it is")   
se = selectionSort()
se.sort(arr)
se.display(arr)