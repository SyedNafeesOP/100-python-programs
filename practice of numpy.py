# numpy create null vector
import numpy as np

vector=np.zeros(10)
print(vector)

#numpy print function doc

#np.info(np.add)

# numpy create vector with value range
vector=np.arange(22,50)
print(vector)

#numpy reverse method

vector=np.arange(20)
vector=vector[::-1]
print(vector)

#numpy create matrix with value range

matrix=np.arange(9).reshape(3,3)
print(matrix)
# create an array using numpy
arr=np.array([1,2,3,4,5])
print(arr)
#create a arrayof random integers

arr=np.random.randint(20,50,10)
print(arr)
# create an array which contain array elements from 10,20

arr=np.arange(10,20)
print(arr)

#create a one dimential array and convert into 3X3 matrix

arr=np.arange(1,10).reshape(3,3)
print(arr)

#create an array which contains value os 5,10
arr=np.ones(10)*5
print(arr)

#create an array and then convert all the even numbers with 0
arr=np.arange(1,11)
arr[arr%2==0]=0
print(arr)
