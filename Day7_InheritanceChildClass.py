from Day7_OopsDemo import calculator #import parent class "calculator" from file "Day7_OopsDemo.py"


class ChildClass(calculator): #syntax to import the parent class
    num2=50

    def __init__(self): #always the first step is to call the Parent class constructor. so create a new child class constructor
        calculator. __init__(self)  #initializing parent class constructor

    def getcompletedata(self):
        return self.add()+ self.num2

obj = ChildClass()
print(obj.getcompletedata()) #50+ two variables entered by the user from parent class
