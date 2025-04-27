# name=input()
# place=input()
# print("my name is",name)
# print("my place is",place)

# li=[]
# n=int(input("enter nmbr:"))
# for i in range(n):
#     temp=input()
#     li.append(temp)
# print(li)    

# li=[]
# n=int(input("enter nmbr:"))
# for i in range(n):
#     temp=int(input())
#     li.append(temp)
# print(li)    

# s="1 4 7"
# temp=s.split()
# print(temp)

# li=[]
# s="1 3 4"
# temp=s.split()
# for i in range(len(temp)):
#     val=int(temp[i])
#     li.append(val)
# print(li)    


# temp="5 4 3".split()
# print(temp)



# li=list(map(int,input().split()))
# print(li)

# l=int(input())
# u=input()
# li=list(map(int,input().split()))
# f=input()
# print(l)
# print(u)
# print(li)
# print(f)

# li=["1 3 5"]
# res=list(map(int,input.split()))
# print(res)

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# li=[1,2]
# li[0],li[1]=li[1],li[0]
# print(li)

# li=[6,3,89,2,1,78]
# n=len(li)
# for i in range(0,n-1):
#     didswapped=False
#     for j in range(0,n-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
#             didswapped=True
#     print(li)
#     if(didswapped==False):
#          break
# print(li)    

# ls=["hello","bollo","hello","delhi","hello"]
# d={}
# for i in ls:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1    
# print(d)            

# def majority(nms):
#     d={}
#     for i in nms:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1 
#     return d              
# nms=[2,2,1,3,2,4,5,6,7]
# r=majority(nms)
# print(r)

# nums=[1,2,3]
# n=len(nums)
# pairs=0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if(nums[i]==nums[j]):
#             pairs+=1
# print(pairs)

# def sockMerchant(n, ar):
#     pairs=0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if ar[i]==ar[j] :
#                 pairs+=1
#     return pairs   
# n=9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# res=sockMerchant(n,ar)
# print(res)

# def sockMerchant(n, ar):
#     d={}
#     pairs=0
#     for i in ar:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     for count in d.values():
#         pairs+=count//2
#     return pairs
# n=9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# res=sockMerchant(n,ar)
# print(res)       

# key = "the quick brown fox jumps over the lazy dog"
# dict={}
# temp=97
# for i in key:
#     if i!=" " and i not in dict:
#         dict[i]=chr(temp)
#         temp+=1  
# message = "vkbs bs t suepuv"
# ans=""
# for i in message:
#     if i==" ":
#         ans+=" "
#     else:
#         ans+=dict[i]    
# print(ans)    

key = "the quick brown fox jumps over the lazy dog"
dict={}
temp=97
for i in key:
    if i!=" " and i not in dict:
        dict[i]=chr(temp)
        temp+=1
message = "vkbs bs t suepuv"
ans=""
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dict[i]
print(ans)            

          