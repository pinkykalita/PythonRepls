#function is a group of related statements that perform a specific task

#Simple function
def demo_function(): #defining a function
    print("Hello") #this is function body

demo_function() #this is to call the function


#parameterised function:
def demo_paramfunction(name):
    print("this is parameterised function demo "+name)

def add_function(a, b):
    print(a+ b)

demo_paramfunction("Pinky Kalita")#send the string parameter while calling the function
add_function(5, 23)


#returning value from function
def subtractdemo(i, j): #catching the value in i and j
    return i-j #returns the subtract value

print(subtractdemo(45,6)) #print the subtract value
