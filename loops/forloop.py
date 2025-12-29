    #We use a for loop when we want to repeat the same task multiple times without writing the code again and again.
    #We use a for loop when we want to repeat the same task multiple times without writing the code again and again.
for v in "apple": #here i is a variable ,we can give any variable name like mani,i,etcc..
    print(v) 

for i in range (5): # here the value start from 0 and end in 4 , we can set the staring range also 
    print (i)

#1 to print a table by using for loop
for mani in range(1,11):# the range start from 1 ane end with 11
    print("1*2=",mani*2) #here we print table format in range and the range mutiple by 2


#2 using list in loop example
a=["a","p"]
a.insert(0,"m")
print(a)
for i in a:
    print(i)

#2 for using a dict in for loop example
maran={
      "A":{"name":"manimaran","age":"20","department":"ai"},
      "B":{"name":"harini","age":"22","department":"ece"}
}
for a,b in  maran.items():
    print(a)
    for m,k in b.items():
        print(m,":",k)

#for loop examples
# count the number of letter in words manimaran
a="manimaran"
b=0
for i in a:
    b=b+1
print(b) 

 #count the how many vowels in a letter
a="manimaran"
b="aeiou"
c=0
for i in a:
    if i in b:
        c=c+1
print(c)

#count how many digits in a string
a="abc123"
b=0
for i in a:
    if i.isdigit():
        b=b+1
print(b)    

for i in range (5): # here the value start from 0 and end in 4 , we can set the staring range also 
    print (i)

    #1 to print a table by using for loop
    for mani in range(1,11):# the range start from 1 ane end with 11
        print("1*2=",mani*2) #here we print table format in range and the range mutiple by 2


    #2 using list in loop example
    a=["a","p"]
    a.insert(0,"m")
    print(a)
    for i in a:
        print(i)

    #2 for using a dict in for loop example
    maran={
        "A":{"name":"manimaran","age":"20","department":"ai"},
        "B":{"name":"harini","age":"22","department":"ece"}
    }
    for a,b in  maran.items():
        print(a)
        for m,k in b.items():
            print(m,":",k)

    #for loop examples
    # count the number of letter in words manimaran
    a="manimaran"
    b=0
    for i in a:
        b=b+1
    print(b) 

    #count the how many vowels in a letter
    a="manimaran"
    b="aeiou"
    c=0
    for i in a:
        if i in b:
            c=c+1
    print(c)

#count how many digits in a string
    m="abc123"
    z=0
    for i in m:
        if i.isdigit():
            z=z+1
    print(z)    

#to print a start pratern using for loop 
for i in range (1): #here i used to  decide  a rows
    for j in  range(5): # here j is used to print the columns
        print("*",end="")# end to used to print in colums 
    print()# its used to go  next line 
    # o|p=*****

#to print a start pratern using for loop 
for i in range (3):
    for j in  range(3):
        print("*",end="")
    print()# o|p=***
                #***
                #***



 #to print 1234
for i in range(1,5):
    print(i,end="")#o/p 1234

# to print the smae number in a each row
for i in range(4):
    for j in range(i):
        print(i,end="")
    print() #1
          #  22
            #333

 #for print *
 #            * *
  #          * * *
  #          * * * *
    for i in range (4):
        if i==0:
            print("*")
    else:
        for j in range(i+1):
            print(" *",end="")
        print()