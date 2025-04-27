def find_factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input("enter nmbr:"))
find_factors(num)            