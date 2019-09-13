with open("demofile2.txt") as f_obj1:
    content1 = f_obj1.read()
with open("demofile1.txt") as f_obj2:
    content2 = f_obj2.read()
content1 = content1.split(" ")
content2 = content2.split(" ")
len1 = len(content1)
len2 = len(content2)
merge = ""
i=0
j=0
while(i<len1 and j<len2):
    str1=content1[i]
    str2=content2[i]
    x = len(str1)
    y = len(str2)
    if(x%2!=0):
        x=x+1
    if(y%2!=0):
        y=y+1
    x=x//2
    y=y//2
    merge+=str1[:x]
    merge+=str2[:y]
    merge+=" "
    i=i+1
    j=j+1
if(i<len1):
    str1=content1[i]
    merge+=str1[:len(str1)//2]
    i=i+1
if(j<len2):
    str2=content2[i]
    merge+=str2[:len(str2)//2]
    j=j+1
print(merge)
with open("file3.txt","w") as f:
    f.write(merge)
