#List that have only integers:
a=[1,9,7,8]
print (a)

#list with only characters
b=['pinky','Krishna', 'D', 'K',"last character of the list"]
print (b)

#list with int and characters
c=[1,2,3,"l","m"]
print(c)

#to print as per the index
print(a[0])#1
print(b[1])#Krishna
print(c[3])#l

#to print last index of the list(in case there are many items
print(b[-1])#last character of the list

#To print from inbetween from the list in a range
print(c[1:4])#this will print [2,3,'l'] Note c[4] is exclusive means 4th character will not print. it will print till 4th

#to insert into the list
a.insert(2,"Krishna")#insert Krishna in list=a at 2nd index=after 9
print(a)#[1,9,'Krishna',7,8]

#to add value at the end of the list
b.append("this is new value at the end")#
print(b)#['pinky', 'Krishna', 'D', 'K', 'last character of the list', 'this is new value at the end']

#To completely replace and update a value
a.insert(2,"KRISHNA")
print(a)#[1, 9, 'KRISHNA', 'Krishna', 7, 8]
a[3]="KRISHNA"
print(a)#[1, 9, 'KRISHNA', 'KRISHNA', 7, 8]
a[2]="VEDANT"
print(a)#[1, 9, 'VEDANT', 'KRISHNA', 7, 8]

#to add/extend multiple values to the list
x = [45, 46]
x.extend(["hello", 48])
print(x)#[45, 46, 'hello', 48]
x.extend([49, "World", 51])
print(x)#[45, 46, 'hello', 48, 49, 'World', 51]
x.extend(range(52, 54))
print(x)#[45, 46, 'hello', 48, 49, 'World', 51, 52, 53]

#to delete a value from the list
del x[0]
print(x)# [46, 'hello', 48, 49, 'World', 51, 52, 53]
del x[-4]
print(x)#[46, 'hello', 48, 49, 51, 52, 53] deleted 4th value from back side
del x[2:5]
print(x)#[46, 'hello', 52, 53]

#to concatenate list
print(a+b)#[9, 'VEDANT', 'KRISHNA', 7, 8, 'pinky', 'Krishna', 'D', 'K', 'last character of the list', 'this is new value at the end']

#tuples are same as list but they are immutable (uneditable)
tupleexample = (100, 200, "hello")
print (tupleexample)#(100, 200, 'hello')
#tupleexample[2] = "pinky"
#print (tupleexample)#'tuple' object does not support item assignment

#Dictionary: to extract/read value from a dictionary call using the corresponding key
dict = {"a":123, "b":1, "c":"hello", 4:1000 }
print(dict[4])#1000 -> key 4 has velue 1000, it is not ased on index
print(dict["c"])#hello ->redaing dictionary value of key c

#Dictionary: to insert data to the dictionary in run time
new_dict = {} #first define an empty dictionary
new_dict[1]="pinky kalita" #defing key 1 and assigning value "Pinky kalita"
new_dict["age"] = 34 #defining key "age" and assigning value 34
print(new_dict) #{1: 'pinky kalita', 'age': 34}
print(new_dict[1]) #pinky kalita ->reading value of key 1
