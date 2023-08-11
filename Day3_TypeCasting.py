#Type casting: to concatenate 2 different data types
a=5
b="text"
#to check the type of variable use type()
print(type(b))
print("_______________")
# print("hi"+ a) #if we print this line there will be TypeError as string cannot be concatenated with int or float. Here we can use TypeCasting


#Using str(), Int(), Float()
print("Hi" + str(a)) #here a is getting conversted to string and concatenated with Hi
print(5+float(a)) #a is converted to float and then added to 5
print(str(a) + b) #int is converted to string
print("_______________")


#using "{}{}".format()
i = "integer_value: "
j = 23
print("{}{}".format(i,j))
print("_______________")


#using %s & %d
l = "laugh_out_loud"
m = 5
print("hi %d %s" % (m, l)) #%d denotes int type and %s denotes string type
print("_______________")









