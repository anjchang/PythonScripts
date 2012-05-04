#Opens a file and saves what you write to it.

filename = "test.dat"
done = 0
namelist = []
while True:
    name = raw_input("Enter a name:")
    if name:
        # print type("")
        #print type(name)
        #print type(name) == type("")
        namelist.append(name)
    else:
        break
FILE1 = open(filename,"w")
FILE1.writelines(namelist)
for name in namelist:
    FILE1.write(name)
FILE1.close()
