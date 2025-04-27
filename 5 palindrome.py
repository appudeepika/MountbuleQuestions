num=int(input("enter nmbr:"))
res=0
temp=num
while(num>0):
    rem=num%10
    res=res*10+rem
    num=num//10
print(res)   
if res==temp:
    print("palindrome")
else:
    print("not palindrome")    

#reverse of a number
def reverse_nmbr(num):
    res=0
    temp=num
    while(num>0):
        rem=num%10
        res=res*10+rem
        num=num//10
    print(res)
    if res==temp:
        print("palindrome")
    else:
        print("not palindrome") 

num=int(input("enter nmbr:"))
reverse_nmbr(num)            

