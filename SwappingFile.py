def swapFileData():
    input1 = input("What is the name of the first file?")
    input2 = input("What is the name of the second file?")
    print(input1)
    s1=open(input1)
    filelines1 = s1.read()
    s2=open(input2)
    filelines2 = s2.read()
    print(filelines1,filelines2)
    write1=open(input1,"w")
    write1.write(filelines2)
    write2=open(input2,"w")
    write2.write(filelines1)
swapFileData()      