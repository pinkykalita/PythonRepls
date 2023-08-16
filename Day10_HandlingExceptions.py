# Exceptions to validate the test scenarios

# using raise exception

items = 0
if items !=2:
   # raise Exception("Items in cart does not match")
    pass # to go to the next code block use pass keyword which will pass this code block


# using assert

itemsincart = 5
#assert (itemsincart == 2) # if itemsincart is not equal to 2 then AssertionError will be thrown
pass


# using try except mechanism
# when we know that a specific code will fail and we don't want the code execution to stop
# then we can put that exception in try block and test will be written in except block

try:
   with open("testtextfile.txt") as f:
       f . read()
       print("there is no exception while executing this try block")
except:
    print("An exception was thrown")


# to catch the actual error thrown by Python
try:
    with open ("filename.txt") as fileobj:
        fileobj . read()
except Exception as e:
    print(e) # No such file or directory: 'filename.txt'


# finally keyword
# we can use this block to clean up the resources/cookies no matter the code pass or fails
try:
    with open ("filename.txt") as fileobj:
        fileobj . read()
except:
    print("this is to demo finally keyword")
finally:
    print("This block will be executed irrespective of code pass or failure")



