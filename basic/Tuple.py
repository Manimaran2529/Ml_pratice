#//Tuple:
      #// is not a mutable  we cannot insert, pop the values,
     #// its also allow the duplicate 
     #// any datatypes we can use like init,float,etc..
#//Symbol=>()
 #//example:
a=(1,2,3)
print(a) #// o/p:[1, 2, 3]

#// we can use the tuple as mutable by converting into a list 
a=(1,2,3,4)
b=list(a)#//convert into a list so we can use tuple as mutable
b.append(10)
print(b)