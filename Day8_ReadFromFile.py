open("testtextfile.txt")#directly file name as text file is in same location as the .py file
#this method to first open the file

#now create a file object to access the file contents
fileobj = open("testtextfile.txt") #now fileobj has all the knowledge of the file

#to read specific characters of the file
print(fileobj.read(15)) #prints first 15 characters in the file
print("-----------------")

#to read one lines in file
print(fileobj.readline()) #after reading first 15 character now the pointer is at the end of the 15th char so next line will be printed
print(fileobj.readline())
print("-----------------")

#to read the lines in file
print(fileobj.read()) #entilre file content will be printed on the console
print("-----------------") #At this stage the fileobj cursor is at the end of the second line because of readline cmd
#so the remaining file content will be read

#always close the file to avoid memory leak
fileobj.close()




