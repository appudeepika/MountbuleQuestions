def check_prime(num):
    for i in range(2,num+1):
        if num%i==0:
            return False
        else:
            return True
num=int(input("enter nmbr:"))
res=check_prime(num)        
if res==True:
    print("it is a prime nmbr")
else:
    print("not a prime nmbr")    
