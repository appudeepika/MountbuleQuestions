# li=[5,9,1,8,7]
# n=len(li)
# l=0
# temp=0
# k=3
# ans=0
# for r in range(n):
#     temp+=li[r]
#     if(r-l==k):
#         temp-=li[l]
#         l+=1
#     if(r-l+1==k):
#         ans=max(ans,temp)
# print(ans)            

# sunstring of size three with distinct charachets
# li="xyzzaz"
# n=len(li)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(li[k])
#         if len(temp)==3 and len(set(temp))==3:
#             ans+=1
# print(ans)            


# s="aababcabc"
# n=len(s)
# ans=0
# l=0
# li=[]
# k=3
# for r in range(n):
#     li.append(s[r])
#     if r-l==k:
#         li.pop(0)
#         l+=1
#     if r-l+1==k:
#         print(li)

# li="abcabderf"
# n=len(li)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(li[k])
#         if len(temp)==3 and len(set(temp))==3:
#             print(temp)
       
s= "xyzzaz"
n=len(s)
dict={}
l=0
k=3
res=0
for r in range(n):
    if s[r] in dict:
        dict[s[r]]+=1
    else:
        dict[s[r]]=1    
    if r-l==k:
        dict[s[l]]-=1
        if dict[s[l]]==0:
            dict.pop(s[l])
        l+=1
    if len(dict)==k:    
        res+=1
print(res)        


# u are given an array and you  shoild find the max len of the subarray which has atmost k odd nmbres k=2
arr=[0,1,3,1,1,6,7,1,0,1]
n=len(arr)
k=2
l=0
temp=0
ans=0
for r in range(n):
    if arr[r]%2!=0:
        temp+=1
    while temp>k:
        if arr[l]%2!=0:
            temp-=1
        l+=1    
    ans=max(ans,r-l+1)
print(ans)        
