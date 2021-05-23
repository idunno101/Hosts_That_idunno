import os

firstfile = "./Domains/" + os.environ['OUTPUT_FILE']
secondfile = os.environ['SUPPLIED_FILE']

f1 = open(firstfile, 'w')
f2 = open(secondfile, 'r')
    
for line in f2:
    if line != 'null\n':
        f1.write("0.0.0.0  " + line)
 
f1.close()
f2.close()
