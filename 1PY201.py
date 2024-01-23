data = input()  
s=0
n=0
i=0
while data:
    i=i+1
    ls=data.split()
        s=s+int(ls[2])
        if ls[1]==('男'):
            n=n+1   
    data = input()
s=s/i
print("平均年龄是{:.2f} 男性人数是{}".format(______))
