import sys
import numpy as np
import time
list1=range(100)
arr1=np.array(100)
print(sys.getsizeof(1)*len(list1))
print(arr1.itemsize*arr1.size)
x=range(1000000)
y=range(2000000,300000)
start_time=time.time()
c=[(x,y) for x,y in zip(x,y)]
print("Time taken by list operation:",(time.time()-start_time)*1000)
np1=np.arange(1000000)
np2=np.arange(2000000,3000000)
start_time=time.time()
np3=np1+np2
print("Time taken by numpy operation:",(time.time()-start_time)*1000)
