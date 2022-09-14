lst=[]

a=int(input("enter the list limit"))
for i in range(0,a):
      b=int(input("enter element:"))

      lst.append(b)
print(lst)
def squaresum(a):
    odd=0
    even=0
    for i in a:
        if(i%2==0):
             even=even+i**2
        else:
             odd=odd+i**2
    a=[odd,even]
    return a

print(squaresum(lst))
