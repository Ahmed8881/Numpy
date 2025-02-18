import sys
import numpy as np
list1=range(100)
arr1=np.array(100)
print(sys.getsizeof(1)*len(list1))
print(arr1.itemsize*arr1.size)

