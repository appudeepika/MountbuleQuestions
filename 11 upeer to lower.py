str=input("enter string:")
res=""
for i in str:
    ascii=ord(i)
    if(ascii>=65 and ascii<=90):
        newascii=ascii+32
        convchar=chr(newascii)
        res=res+convchar
    else:
        res=res+i
print(res)            


def conver_upper_lower(str):
    res=""
    for i in str:
        ascii=ord(i)
        if(ascii>=65 and ascii<=90):
            newascii=ascii+32
            conchar=chr(newascii)
            res=res+conchar
        else:
            res=res+i
    print(res)
str=input("enter string:")
conver_upper_lower(str)          


# conerting lower to upper case
def convert_lower_upper(str):
    res=""
    for i in str:
        ascii=ord(i)
        if(ascii>=90 and ascii<=122):
            newascii=ascii-32
            conchar=chr(newascii)
            res=res+conchar
        else:
            res=res+i
    print(res)
str=input("enter string:")
convert_lower_upper(str)   

# upper to lower and loer to upper
def conver_upper_lower(str):
    res=""
    for i in str:
        ascii=ord(i)
        if(ascii>=65 and ascii<=90):
            newascii=ascii+32
            conchar=chr(newascii)
            res=res+conchar
        elif(ascii>=90 and ascii<=122):
            newascii=ascii-32
            conchar=chr(newascii)
            res=res+conchar   
        else:
            res=res+i    
    print(res)
str=input("enter string:")
conver_upper_lower(str)    