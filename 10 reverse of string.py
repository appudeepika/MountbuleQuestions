def reverse_string(str):
    res=""
    for i in str:
        res=i+res
    print(res)
str=input("enter string:")
reverse_string(str)        