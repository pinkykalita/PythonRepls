# extract the file content
# reverse the file content and write it back to the same file


with open("testtextfile.txt", "r") as fileobject:  # with keyword will auto close the file
    content = fileobject . readlines() # [cat, dog, document, test]
    rev_content = reversed(content) # reverse the file content
    with open("testtextfile.txt", "w") as writerobj: # to make the file writable open in "w" mode
        for line in rev_content:
            writerobj . write(line) # [test, document, dog, cat]


