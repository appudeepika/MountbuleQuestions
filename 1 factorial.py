def factorial(num):
    if num<0:
        return "Factorial does not exist fror negative nmbrs"
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter nmbr:"))
res=factorial(num)
print(res)    
print(f"the factorial of {num} is {res}")