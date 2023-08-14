class calculator:
    userdata1 = input("Enter any number: ") #this is a class variable: defined inside a class
    a = int(userdata1)
    userdata2 = input("Enter another number: ")
    b = int(userdata2)

    def __init__(self):    #syntax to declare a constructor
        print("Constructor is called automatically as soon as an object of a class is declared")
        number1 = 5#syntax to define instance variable
        print(number1) #This is an instace variabl: defined inside a constructor


    def add(self):
        #return a+b #variables cannot be called directly inside a function in Python.
        #use self keyword to access the instane variable
        #use classname or self to access the class variable
        return calculator.a + self.b

    def subtraction(self, x, y):  #syntax to catch the params sent while calling the function
        self.var1 = x  #syntax to initialize a new instace variable to store the passed param
        self.var2 = y
        return self.var1 - self.var2

calobj = calculator() #syntax to define a new object. No need of "new" keyword
summation = calobj.add()
print("The sum of the numbers are: " + str(summation))

subtraction = calobj.subtraction(9,4)  #syntax to sent the parameters while calling the subtraction function
print("The subtraction of the numbers are:"+ str(subtraction))




