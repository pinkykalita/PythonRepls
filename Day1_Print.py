#Basic print function
print("Hi i am learning\nPython")  #use of new line \n
print("This is how" + " strings are " + "concatenated")  #to concatenate use +

#Data types/Variables
name = input("What is your name? ")  #input(prompt) function takes user's input
print("Hello " + name + " " + input("What is your Surname? ") +"!")  #this will take user input(name)and print Hello name!

#Defining multiple variables in single line
b, c, d = "this", 4, "text"
print(b, c, d)

#Get name input and print all characters in the name 1 by 1
name = input("What is your Country Name? ")
for i in name:
    print(i)


#Get name from user then count and print the total characters in the user input
City = input("What is your City? ")
n = len(City)
#print("your city ha"+n+"characters")#This will throw TypeError as int cannot be concatenated with string
print("Your City has " + str(n) + " characters in its name")  #for int to str parsing use str(INT object) function


#Swap variable values
a=input("a: ")
b=input("b: ")
c=a #assigning a value to another var c
a=b #Now assigning b value to a
b=c #assigning a value to b
print("a: "+a)
print("b: "+b)


#Band name generator
city=input("Enter your city name:\n") #putting \n will bring the input cursor to next line
pet=input("Enter your pet name:\n")
print("your band name:"+city+pet) #concatenate City and Pet name




