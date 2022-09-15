def sq(n):
    if(n<=3):
        return n
    res=n
    for i in range(1,n+1):
        temp=i*i
        if temp>n:
            break
        else:
            res=min(res,1+sq(n-temp))
    return res
num=int(input("enter:"))
print(sq(num))
