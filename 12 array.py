array=[]
for i in range(5):
    nmbr=int(input("enter nmbr:"))
    array+=[nmbr]
print(array)  

array=[]
for i in range(5):
    nmbr=int(input("enter nmbr:"))
    array.append(nmbr)
print(array)    

# taking the range value from user
def array_enter(num):
    array=[]
    for i in range(num):
        nmbr=int(input("enter nmbr:"))
        array+=[nmbr]
    print(array)
num=int(input("enter the range:"))
array_enter(num)        