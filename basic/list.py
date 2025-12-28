#//list:
  #//list is mutable we can change the values, and its allow the duplicate values like ,1,1,2 
  #we can use the any datatypes in the list like;"1","mani","0.1"
  
# Symbol=>[]

#//example:
a=[1,2,3]

print(a) #// o/p:[1, 2, 3]
 
#//add the values in the list at end
#//example:
a=[1,2,3]
a.append(10)
print(a) #// o/p:[1, 2, 3, 10]

#//add the element in  anywhere by using index value:
#//example 1:
a=[1,2,3]
a.insert(1,10)#here 1 is a index value 
print(a)#//o/p:[1, 10, 2, 3]
#// example2 :
a=[1,2,3]
a.insert(3,22)#here 3 is a index value 
print(a)#// o/p:[1,2,3,22]

#//delete the values in the list:
#// Example 1:
a=[1,2,3,33]
a.pop(0)# here 0 is a index value  we delete the value by using index value
print(a)#// o/p:[2,3,33]

#//remove the values in the list at end
a=[1,2,3,33]
a.pop()
print(a)#// o/p:[1,2,3]


#//merger the two list:
#//Example 1:
a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(a) #// o/p:[1,2,3,4,5,6,7,8]
#// Example 2:
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10]
a.extend(c)
print(a) #// o/p:[1,2,3,4,9,10]

#//summary:add we use insert(1,10),append for last
      #// :delete we use the pop(1),pop() for last
      #// :for merger the list we use extend
