#// dictonary not allow duplicate 
#// its a mutable  we  can chnage the data 
#// any datatypes can be stored 
#// its an oder 
 #// symbol:
mani={
    "maran":["1","2","3"]#// here maran is keys and 1,2,3 is values
  }
print(mani)#// o/p"maran":["1","2","3"]


 #//  to print only the values
mani={
    "maran":["1","2","3"]#// here maran is keys and 1,2,3 is values
  }
print(mani.keys)#// o/p"maran"


 #//  to print the values in the dictionary
mani={
    "maran":["1","2","3"]#// here maran is keys and 1,2,3 is values
  }
print(mani.values)#// o/p["1","2","3"]

 #// change the values in the dictionary
mani={
    "maran":["1","2","3"]#// here maran is keys and 1,2,3 is values
  }
mani["maran"]="mani"
print(mani)#// o/p"maran":["1","2","3","mani"]  


#// add the  keys and values in the dictionary
mani={
    "maran":["1","2","3"]#// here maran is keys and 1,2,3 is values
  }
mani["yogana"]="mani"
print(mani)#// o/p"maran":["1","2","3"],"yogana":["mani"]  

 #// delete  the values in the dictionary
mani={
    "maran":["1","2","3"],#// here maran is keys and 1,2,3 is values
    "mai":["mm"]
  }
mani.pop("mai")
print(mani)#// o/p"maran":["1","2","3","mani"]     
