# Pandas is a Python library used for data analysis and data manipulation.Pandas is a Python library used for data analysis and data manipulation.
#Why Pandas is used?
#Pandas is mainly used to:
#📊 Read data (CSV, Excel, JSON)
#🧹 Clean data (remove errors, missing values)
#🔍 Filter and analyze data
#➕ Add, remove, or modify columns
#📈 Prepare data for Machine Learning


#Function  Purpose
#head()     First rows
#tail()    Last rows
#info()    Structure & datatypes
#describe()  Statistics
#shape      Size
#columns    Column names

#example  1 create pandas for read a data in dict
import pandas as pd
mani={
    "A":[ "manimaran","Ai/ds","4th year"],
    "B":["harini","ece","4th year"]
}
pm=pd.DataFrame(mani)
print(pm) 


#Example 2  add a new columns in a dictionary by using pandas and change the index value 
import pandas as pd
mani={
    "A":["mani","Ai","4th year" ],
    "B":["yogana","Agri","5th year"]
}
km=pd.DataFrame(mani, index=("name:","department:","year:")) #this is used for assign the rows in the datafram
km["C"]=["harini","Ece","4th year"]#this line is used for add the new  datasets in the datasets 
print(km)


#Example 3  add a new row in a dictionary by using pandas and change the  row value 
import pandas as pd
mani={
    "A":["mani","Ai","4th year" ],
    "B":["yogana","Agri","5th year"]
}
km=pd.DataFrame(mani,columns={"A":"1","B":"2"}) #this is used for assign the columns in the datafram
km["C"]=["harini","Ece","4th year"]#this line is used for add the new  datasets in the datasets 
print(km)


#Example 4:  read a file using a  pandas 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")#i this we change pd.read_csv or excel based upon the filr type
print(mm.head())# head is used print the first 10 line and we use tail is used for print last 10 lines


#example 5: check the null values in a datasets 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")
print(mm.isna().sum())# isna is full form isnull check the null values and .sum() is show the null value in total


#example 5: fill  the null values in a datasets 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")
manim=mm.fillna("mani")# here fillna command is used for  fill the  null values here  if the datasets we want we use filna  
print(manim.head())

# we did not the use the inplace function its changed the original datasets

#example 6 : if we want t0 compare the original datasets and change datasets  
# 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")
manim=mm.fillna("mani")
print(mm.head())

print(manim.head())


#example 7:  delete  the null values in a datasets 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")
manim=mm.dropna()# here dropna function is used to delete the null values in the datasets 

print(manim.head())

#example 8:  delete  the repeat values in a datasets 
import pandas as pd
mm=pd.read_csv("C:\Mypc\Projects\ml paratice\loops\Housing.csv")
manim=mm.drop_duplicates() # its used to remove the data when its repeat again 

print(manim)

