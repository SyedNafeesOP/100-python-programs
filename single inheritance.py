class Iphone:
    def __init__(self,name,processor):
       self.name=name
       self.processor=processor
    def show_details(self):
        print(f"name of model is\t{self.name}")
        print(f"processor of phone is\t{self.processor}")
        print("its my favourite phone")

I1=Iphone("iphone 11","A13 Bionic chip")
I1.show_details()

class Android(Iphone):
    def __init__(self,name,processor):
        self.name=name
        self.processor=processor
    def show_details(self):
        print(f"name of model is \t {self.name}") 
        print(f"name of model is \t{self.processor}")
        print(" I want to compare these two phone but my favourite is iphone")
A2=Android("Samsung a 52","Snapdragon 720G processor." )
A2.show_details()



