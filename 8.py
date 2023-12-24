# program to find largest among three number
num1=int(input("Enter first number :\n"))
num2=int(input("Enter second number :\n"))
num3=int(input("Enter  third number :\n"))
if (num1>num2) and (num1>num3):
    print(num1,"is a largest number ")
elif (num2>num1) and (num2>num3):
     print(num2,"is a largest number ")
else:
    print(num3,"is a largest number ")     