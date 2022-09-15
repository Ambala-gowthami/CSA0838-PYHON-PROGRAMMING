l=[]
r=int(input("Enter Range :"))
for i in range(r):
    i=int(input("Enter: "))
    l.append(i)
print(l.index(max(l)))
