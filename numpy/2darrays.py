# 2D array (Two-Dimensional Array) is a collection of data arranged in rows and columns
#just like a table or a matrix
#Data is in table form
#You need rows + columns
#You are working with datasets
#You are learning ML, AI, Data Science
#row=0
#cloumn=1

#Example 1:structure of a 2d array
import numpy as pd
mm=pd.array([[10,20,29],[10,60,60]])
print(mm)# size is used for a number of elments in a array,ndim is used for a check the dimensio of the array

#example 2: print the  select  number in a array 
import numpy as ps
mani=ps.array([[10,20,30],[10,80,90]])
print(mani[0][1]) #here 0 is a array index and 1 is index value in 0 array

#example 3: add the new  value  in the rows

import numpy as pd
mani=pd.array([[10,20,30],[70,60,80]])
maran=pd.append(mani,[[30,40,50]],axis=0)
print(maran)
 

#exmaple 4:add the new values in the columns import numpy as pd
mani=pd.array([[10,20,30],[70,60,80]])
maran=pd.append(mani,[[30],[40]],axis=1)
print(maran)

#example 5:delete  the value in the coloum
import numpy as np
mani=np.array([[10,20,40],[50,60,70]])
maran=np.delete(mani,0,axis=1)
print(maran)


#example:6 dele the values in the row 
import numpy as np
mani=np.array([[10,20,40],
               [50,60,70]])
maran=np.delete(mani,0,axis=0)
print(maran) 

#example7:indexing
import numpy as np
mani=np.array([[10,20,40,50],
              [50,60,80,90],
              [12,20,44,55]])
print(mani[0][0])
print(mani[1][0])
print(mani[2][0])

#example8:slicing
import numpy as np
mani=np.array([[10,20,30],
               [10,20,30],
               [10,20,30]])
print(mani[0,0:2])
print(mani[1,0:2])
print(mani[2,0:2])


#example9:print only the rows
import numpy as np
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

print(arr[:,1])#print the  row only o/p[20,50,80]

