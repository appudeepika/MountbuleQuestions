def even_odd(num):
    if num%2==0:
        print(f"the number {num} is even")
    else:
        print(f"the number{num} is odd")
num=int(input("enter nmbr:"))
even_odd(num)            
    
# even nmbrs with in a range
def even_nmbrs(start,end):
    for num in range(start,end+1):
        if num%2==0:
            print(num,end=" ")
        print()    
start=int(input("enter nmbr:"))
end=int(input("enter nmbr:"))
even_nmbrs(start,end)            

# odd nmbrs with in a range
def even_nmbrs(start,end):
    for num in range(start,end+1):
        if num%2!=0:
            print(num,end=" ")
        print()    
start=int(input("enter nmbr:"))
end=int(input("enter nmbr:"))
even_nmbrs(start,end)            

            