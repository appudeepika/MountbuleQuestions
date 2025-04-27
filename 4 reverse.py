num=int(input("enter nmbr:"))
res=0
while(num>0):
    rem=num%10
    res=res*10+rem
    num=num//10
print(res)    

#reverse of a number
def reverse_nmbr(num):
    res=0
    while(num>0):
        rem=num%10
        res=res*10+rem
        num=num//10
    print(res)
num=int(input("enter nmbr:"))
reverse_nmbr(num)            
