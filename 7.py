#program to check  leep number
year=int(input("enter a year:\n"))
if(year % 400 == 0) and (year % 100 == 0):
    print(year, "it is a leep year")
elif year % 4== 0 and year % 100 !=0:
    print(year, "it is a leep year")
else:
    print(year, "it is not a leep year")


