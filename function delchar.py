s=str(input("sentence: "))
r=input("The character to be removed : ")
sp=""
for i in (s):
    if(i==r):
        continue
    else :
        sp=sp+i
print(sp)
