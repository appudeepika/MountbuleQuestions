num=int(input("enter nmbr:"))
res=0
digit=len(str(num))
temp=num
while(num>0):
    rem=num%10
    res=(rem**digit)+res
    num=num//10
if res==temp:
    print("Armstrong nmbr")
else:
    print("not armstrong")        