#if else condition
a = input("Enter any number ")
x = int(a)
b = input("Enter any number ")
y = int(b)
if x < y: #always put a : that shows that curly bracket starts here as there is no opening and closing braces for a condition/loop in Python
    print(str(x) + " is less than " + str(y)) #indentation is mandatory
else: #same from here the else block will start so a :
    print(str(x) + " is greater than " + str(y))
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





