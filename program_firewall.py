inputfile = "./secure"

myfile = open(inputfile, 'r', 'utf_8')
for line in myfile:
    if "ssh" in line:
        
