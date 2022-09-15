g=input("enter the Grade(A/B) : ")
s = int(input("salary : $ "))
if(g =='A' and s <= 10000):
    print("Total salary : $ ",(s//7)+s)
elif(g =='A' and s > 10000):
    print("Total salary : $ ",(s//5)+s)
elif(g =='B' and s <= 10000):
    print("Total salary : $ ",(s//12)+s)
elif(g =='B' and s > 10000):
    print("Total salary : $ ",(s//10)+s)
else:
    print("wrong input")
