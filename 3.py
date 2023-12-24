#program to swap two variables
# by using third variable
x=13
y=12

temp=x
print("the value of temporary variable is ",temp)
x=y
print("the value of x is ",x)

y=temp
print("the value of y is",y)


# without using third variable
x=12
y=13
x,y=y,x
print('the value of x is ',x)
print('the value of y is ',y)
