# lab03 tests

import labs.lab03 as lab


#open text file in read mode
text_file = open(lab, "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
print(data)