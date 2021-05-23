# entering the file names
firstfile = "1.txt" 
# input("Enter the name of first file ")
secondfile = "2.txt"
# input("Enter the name of second file ")
import os

firstfile = "./Domains/" + os.environ['OUTPUT_FILE']
secondfile = os.environ['SUPPLIED_FILE']

f1 = open(firstfile, 'w')
f2 = open(secondfile, 'r')
    
for line in f2:
    if line != 'null\n':
        f1.write("0.0.0.0  " + line)
 
# closing the files
f1.close()
f2.close()