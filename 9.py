#check a  number prime or not 
num=int(input("Enter a number here :\t"))

if num==1:
    print("it is not a prime number ")
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("it is  not a prime number ") 
        else:
            print("it is  a prime number")    
