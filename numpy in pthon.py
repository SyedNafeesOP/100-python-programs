#single dimensial

import numpy as np 

l1=[1,2,3,4]

n1=np.array(l1)

print(n1)

#multi dimential

n2=np.array([[1,2,3,4],[4,3,2,1]])

print(n2)
print(type(n2))

#initialyzing numpy array with 0

# There is a  method for zeros known as np.zero

f1=np.zeros((1,2))
print(f1)

# in outer program 1,is for row and 2,is for columb

f2=np.zeros((5,5))
print(f2)

# initialyzing numpy arraywithsame number with method np.full

z1=np.full( (4,4),10)
print(z1)

#initializing numpy array with range with method np.arange

z1=np.arange(4,8)
print(z1)

z1=np.arange(4,10,2)
print(z1)

# JOINING NUMPY ARRAY WITH THREE METHODS 
# vstack() in this method array is row wise but not confirm
#hstack() in this method array is horizontly 
#column_stack() in this method array is column vise

# 1st method vstack()
n1=np.array([10,20,30])

n2=np.array([40,50,60])

print (np.vstack((n1,n2)))

#2nd method  hstack()

n1=np.array([50,60,70])

n2=np.array([80,90,70])

print(np.hstack((n1,n2)))

# 3rd method(column_stack())


n1=np.array([50,60,70])

n2=np.array([80,90,70])

print(np.column_stack((n1,n2)))

#Numpy Intersection and diffference
#three methods
#np.intersect1d(n1,n2)

n1=np.array([10,20,30,40,50])

n2=np.array([50,60,70,80,90])

print(np.intersect1d(n1,n2))

#2nd method
#np.setdiff1d(n1,n2))


n1=np.array([10,20,30,40,50])

n2=np.array([50,60,70,80,90])

print(np.setdiff1d(n1,n2))

#3rd method

n1=np.array([10,20,30,40,50])

n2=np.array([50,60,70,80,90])

print(np.setdiff1d(n2,n1))

#Numpy Array Mathematics

#addition of Numpy Array
# by using sum method
#if there is axis=0 now they sum in column vise
#if there is axis=1 now they sum in row vise

f1=np.array([10,20])

f2=np.array([30,40])

print(np.sum([f1,f2]))
# in column vise

print(np.sum([f1,f2],axis=0))

#in row wise
print(np.sum([f1,f2],axis=1))

#basic  Numpy array multiplication

n1=np.array([10,20,30])

n1=n1+1

print(n1)  

n1=n1+1

print(n1)  
n1=n1*5

print(n1)  

n1=n1-1

print(n1)  

n1=n1/2

print(n1)  


