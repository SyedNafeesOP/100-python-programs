#in multiple class two parent and one child class
class Employee:

    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name is {self.name}")


class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"dance is {self.dance}")    

class DancerEmployee(Employee,Dancer):
     def __init__(self,dance,name):
        self.dance=dance
        self.name=name
d1=DancerEmployee("kathak","izzah")
print(d1.name)
print(d1.dance)
d1.show()


