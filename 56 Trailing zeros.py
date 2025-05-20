def traling_zeros(n):
    res=0
    powerof5=5
    while n>=powerof5:
        res=res+(n//powerof5)
        powerof5=powerof5*5
    return res
n=int(input("enter nmbr:"))   
ans=traling_zeros(n)
print(ans)

# hcf
def gcd(a,b):
    min=0
    if a<b:
        min=a
    else:
        min=b
    for i in range(min,0,-1):
        if(a%i==0 and b%i==0):
            return i
a=20
b=15
res=gcd(a,b) 
print(res)              

# hcf
def euclid_gcd(a,b):
    while (a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
a=20
b=15
res=euclid_gcd(a,b) 
print(res)              

# LCM
def lcm(a,b):
    res=max(a,b)
    while(True):
        if(res%a==0 and res%b==0):
            break
        res=res+1
    return res
a=2
b=5
ans=lcm(a,b)
print(ans)    


