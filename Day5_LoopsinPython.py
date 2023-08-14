#if else condition
a = input("Enter any number ")
x = int(a)
b = input("Enter any number ")
y = int(b)
if x < y: #always put a : that shows that curly bracket starts here as there is no opening and closing braces for a condition/loop in Python
    print(str(x) + " is less than " + str(y)) #indentation is mandatory
else: #same from here the else block will start so a :
    print(str(x) + " is greater than " + str(y))
if x ==y:
    print(str(x) + " is same as " + str(y))
print("--------End----------------") #mind the indentation, as it is not a part of the else loop

#for loop
obj = [1, 3, 5, 6, 7]
for i in obj:
    print("numbers in array are: "+ str(i)) #with every iteration i=1, i=3... and that will be printed
for i in obj:
    print(str(i)+ " * 2 = "+str(i*2)) #print each number in array multiplied by 2
print("---------End-------------")

#nested for loop: print multiplication of first 5 natural numbers
nums = [1, 2, 3, 4, 5]
print(nums[0:5]) #just to print all the numbers till 5
multiply_value = 1
for i in nums:
    multiply_value = multiply_value * i
    #print(multiply_value) # this will print the multiplication after each iteration
print(multiply_value) # This will print the total multiplication value (just once at the end) so don't include inside for block
print("-------------------End--------------------")

#sum of first 5 natural numbers
summation = 0
for j in range(1,6): #this is same as for(1=1;i<6;1++)
    summation = summation + j
print(summation)
print("--------------------End----------------")

#print till 10 with increment of 2
for k in range(1,10,2): #for(k=1;k<10;k+2)
    print(k)
for l in range(1, 10, 5):
    print(l)
print("--------End------------")


#while loop: for loop has a range but while works with a condition and untill the condition becomes false
# the loop will keep iterating

numb = 1
while numb<5:
    print(numb)
    numb = numb + 1 #this is equivalent to numb++
print("-----------1st While loop ends here--------------")

new_numb = 6
while new_numb > 1:
    if new_numb == 2:
        break #as soon as new_numb=2, the while loop will be exited, means it will not print last 2 and 1
    print(new_numb) #6,5, 4, 3
    new_numb = new_numb - 1
print("------2nd while loop ends here---------")




