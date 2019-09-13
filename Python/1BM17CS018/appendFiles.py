f = open("demofile2.txt", "a")
f.write("Welcome to BMSCE")

f = open("demofile2.txt", "r")
content=f.read()
for line in content.split(' '):
    first_half = len(line)
    print(line[0:first_half/2])
f2 = open("demofile1.txt", "a")
f2.write("What is your name")
f2 = open("demofile1.txt", "r")
con = f2.read()
for line in con.split(' '):
    first_half = len(line)
    print(line[0:first_half/2])

'''third = open ("new.txt","a")
third.write(data2)'''

f.close()
f2.close()

#open and read the file after the appending:

