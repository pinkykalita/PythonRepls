#print a character at nth position of a string
month = input("Enter any month: ")
length = len(month)
new_length = str(length)
print("you entered month that is " + new_length + " character long")
#i=length-1
#new_num=str(i)
input_num = input("Select any number between 1-" + new_length + (" "))
new_input_num = int(input_num)
#alphabet_place=new_input_num-1
#print("the %dth character in %s is: " % (new_input_num, month)) //new_input_num is int type so use %d

alphabet_place = new_input_num - 1
print("the %sth character in %s is: " % (input_num, month))
for letter in month.split(): #split function slpits the string by default on blank space or any character level
  print(letter[alphabet_place] if alphabet_place < len(letter) else None)
