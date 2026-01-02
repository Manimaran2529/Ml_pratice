#(Numerical Python) is a core Python library for numerical and scientific computing.
# It lets you work efficiently with arrays, matrices, and mathematical operations.
# array can only the the one datatype only 
# array can be fast compare to list 
# its very useful for the ai datasets, Data Analysis ,Machine Learning & AI for train the model very fast 
# we have 1D array [10,20], 2d array [[10,20] ,  3d array [[[10,20] we comsoder the colum and rows brackets for array dimension
#                                     [20,30]]             [10,20]
#                                                           [10,20]]]
 
#1d arrray 
# Example 1  for create 1 D array
import numpy as np
arry=np.array([10,20,20])#this line is used to create a  1 array 
print(arry)
print(arry.shape)# this is used to check the dimensions of the array  we can also use ndim,size

#example 2 add the new data to the 1 D array
import numpy as np  
m=np.array([10,20])
c=np.append(m,30)
print(c) #o/p [10 20 30]
import numpy as pd
mani=pd.array([10,20])
maran=pd.insert(mani,1,0)
print(maran)

#example 3 delete the new data to the 1 D array

import numpy as np
m=np.array([10,20,90])
c=np.append(m,30)
d=np.delete(c,1)# we can delete the number by using index value only 
print(d) #o/p [10,30,90]


#example  indexing means access the one element in a array 
import numpy as np
arry=np.array([10,20,20])#this line is used to create a  1 array 
print(arry[0]) #we print the  single number by using the index value 0 is first element ,-1 is the last element and 

# total  the   numbers present in the array
import numpy as np
mm=np.array([10,20,20])
man=arry.sum()
print(man)#o/p 50



#add some values   for each number  present in the array
import numpy as np
mm=np.array([10,20,20])
print(mm+10)#o/p [20 30 30]


# to print the even number in array
import numpy as pd
mm=arry([1,2,3,4])
mani=arry[arry%2==0]
print(mani)

# to print the odd number in array
import numpy as pd
mm=pd.array([1,2,3,4])
mani=mm[mm%2!=0]
print(mani)

#slicing 
import numpy as pd
mm=pd.array([2,4,6,8,10,12])
print(mm[1:4])