# s=set()
# s.add(10)
# s.add(20)
# print(s)


# num=[1,8,9]
# n=len(num)
# ans=[]
# sum=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(num[k])
#         ans.append(temp)    
# print(ans)     


# str="dep"
# n=len(str)
# for i in range(n):
#     for j in range(i,n):
#         temp=""
#         for k in range(i,j+1):
#             temp+=(str[k])
#         print(temp) 


# highest subarray of lenth 3
nums=[5,9,1,8,7]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(nums[k])
            tsum+=nums[k]
        if len(temp)==3:
            print(temp,tsum)
            ans=max(ans,tsum)
print(ans)                

# sunstring of size three with distinct charachets
li="xyzzaz"
n=len(li)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(li[k])
        if len(temp)==3 and len(set(temp))==3:
            ans+=1
print(ans)            

# or

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
# min difference between highest and lowest b scores(leetcode)
nums=[3,4,8,1,5]
nums.sort()
n=len(nums)
k=3
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(nums[k])
        if len(temp)==k:
            last=temp[-1]
            first=temp[0]
            ans=min(ans,last-first)
print(ans)            
