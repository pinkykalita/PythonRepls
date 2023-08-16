#to read by line we have to manally keep adding readline() that many times
#using while loop to read all the content by line
import fileinput

fileobj = open("testtextfile.txt")
line = fileobj.readline()   # read the first line and store it in variable line
# filecontent = line.rstrip()
#while line != " ":    # until line reaches a blank line the loop will continue
for l in line:
    filecontent = line.rstrip()  # remove all the space from the right
    print(filecontent)
    line = fileobj.readline()   # now after printing first line cursor will move to second line, again as 2nd line!=" ",
    # the while loop will come inside and this time print 2nd line. then the cursor move to 3rd line and will continue til
    # blank line is encountered
fileobj.close()


# to read all lines in the file and store it in list form - readlines()
#readlines() helps to anipulate the content easily as file is stored in list form
fileobject1 = open("testtextfile.txt")
lines = fileobject1 . readlines()
print(lines)
print(lines[1])
lines[0] = "hello world" # update the first line (0th index) in the file with hello world
print(lines)
fileobject1.close()

