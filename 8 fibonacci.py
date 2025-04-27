def febonaci(num):
    a=0
    b=1
    for i in range(num+1):
        print(a)
        res=a+b
        a=b
        b=res
num=int(input("enter nmbr"))
febonaci(num)        