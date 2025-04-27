# def insert_elements(arr,position,ele):
#     new_array=[0]*(len(arr)+1)
#     for i in range(position):
#         new_array[i]=arr[i]
#         new_array[position]=ele
#         for i in range(position,len(arr)):
#             new_array[i+1]=arr[i]
#     return new_array
# arr=[2,3,4,5,6,7]
# position=3
# ele=100
# res=insert_elements(arr,position,ele)
# print(res)        

# def delete_elements(arr,pos):
#     new_arr=[0]*(len(arr)-1)
#     for i in range(pos):
#         new_arr[i]=arr[i]
#         for i in range(pos+1,len(arr)):
#             new_arr[i-1]=arr[i]
#     return new_arr
# arr=[2,3,4,5,6,7]
# pos=3      
# res=delete_elements(arr,pos)
# print(res)  

# def second_largest(arr):
#     if arr[0]<arr[1]:  
#         max1,max2=arr[0],arr[1]
#     else:
#         max1,max2=arr[1],arr[0]
#     for i in range(len(arr)):
#         if arr[i]<max1:
#             max1=max2
#             max1=arr[i]  
#         elif arr[i]<max2:
#             max2=arr[i]
#     return max2
# arr=[1,45,23,78,56,90]
# res=second_largest(arr)
# print(res)              

# def second_min(arr):
#     if arr[0]<arr[1]:
#         min1,min2=arr[0],arr[1]
#     else:
#         min1,min2=arr[1],arr[0]
#     for i in range(2,len(arr)):
#         if arr[i]<min1:
#             min2=min1
#             min1=arr[i]
#         elif arr[i]<min2:
#             min2=arr[i]
#     return min2
# arr=[2,3,4,5,6]
# res=second_min(arr)
# print(res)                    


# def reverse_array(arr):
#     for i in range(len(arr)//2):
#         arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
#     print(arr)
# arr=[10,20,30,40,50]  
# reverse_array(arr)

# def left_rotate(arr):
#     first=arr[0]
#     second=arr[1]
#     for i in range(2,len(arr)):
#         arr[i-1]=arr[i]
#     arr[-1]=first
#     arr[-2]=second
#     return arr
# arr=[1,2,3,4,5]
# res=left_rotate(arr)
# print(res)    

# def right_rotate(arr):
#     last=arr[-1]
#     for i in range(1,len(arr)):
#         arr[i]=arr[i-1]
#     arr[0]=last
#     return arr
# arr=[1,2,3,4,5]
# res=right_rotate(arr)
# print(res)    
# def copy_array(arr):
#     newarr=[0]*(len(arr))
#     for i in range(len(arr)):
#         newarr[i]=arr[i]
#     return f"the old array is {arr} and copy of the array is {newarr}"
# arr=[1,2,3,4,5]
# res=copy_array(arr)
# print(res)    

# def count_even_odd(arr):
#     even_count,odd_count=0,0
#     for i in arr:
#         if (i%2==0):
#             even_count+=1
#         else:
#             odd_count+=1
#     return even_count,odd_count
# arr=[1,2,3,4,5,6,7]
# res=count_even_odd(arr)
# print(res)      


# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# arr=[1,2,3,4,5,6]
# target=10
# res=linear_search(arr,target)
# print(res)    

# def binary_search(arr,tar):
#     left,right=0,len(arr)-1
#     while left<right:
#         mid=(left+right)//2
#         if arr[mid]==tar:
#             return mid
#         elif arr[mid]<tar:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# arr=[2,3,4,5,6,7,8]
# tar=7
# res=binary_search(arr,tar)
# print(res)            

# def fid_first_occurance(arr,tar):
#     last_index=-1
#     for i in range(len(arr)):
#         if arr[i]==tar:
#             last_index=i
#     return last_index        
# arr=[2,4,7,6,2,3]
# tar=2
# res=fid_first_occurance(arr,tar)    
# print(res)

# def find_friquence_count(arr):
#     frq_count={}
#     for i in arr:
#         if i in frq_count:
#             frq_count[i]+=1
#         else:
#             frq_count[i]=1   
#     return frq_count
# arr=[1,4,2,3,5,6,7,4,5,3,8,9,7,5,4]
# res=find_friquence_count(arr)
# print(res)      

# def move_zeros(arr):
#     n=len(arr)
#     count=0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[count]=arr[i]
#             count+=1
#     while count<n:
#         arr[count]=0
#         count+=1
#     return arr 
# arr=[0,2,4,0,5,0,4,7,0]
# res=move_zeros(arr)
# print(res)           

# def max_sum(arr):
#     n=len(arr)
#     max_sum=float('-inf')
#     for i in range(n):
#         for j in range(i,n):
#             current_sum=0
#             for k in range(i,j+1):
#                 current_sum+=arr[i]
#             max_sum=max(current_sum,max_sum)
#     return max_sum
# arr=[-5,7,-3,9,8,-1]
# res=max_sum(arr)
# print(res)            

# 1. Maximum Sum Subarray of Size K
# def max_sum(arr,k):
#     n=len(arr)
#     window_sum=0
#     for i in range(k):
#         window_sum+=arr[i]
#     max_sum=window_sum   
#     for i in range(k,n): 
#         window_sum=window_sum-arr[i-k]+arr[i]
#         if window_sum>max_sum:
#             max_sum=window_sum
#     return max_sum        
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print(max_sum(arr, k)) 
# str=["hello good day","good morning","goog goog goog"]
# ans=0
# for j in range(len(str)):
#     s=str[j]
#     word=1
#     for i in range(len(s)):
#             ch=s[i]
#             if ch==" ":
#                 word+=1
#  
#    ans=max(ans,word)
# def palindrome(x):
#     res=0
#     while x>0:
#         rem=x%10
#         res=res*10+rem
#         x=x//10
#         return True
#     return False
# x=123
# res=palindrome(x)
# print(res)        
# 
# ans=float("-inf")
# li=[-5,-10]
# for i in li:
#     ans=max(ans,i)
# print(ans)    
# min difference between highest and lowest b scores(leetcode)
# nums=[3,4,8,1,5]
# nums.sort()
# n=len(nums)
# k=3
# ans=float("inf")
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(nums[k])
#         if len(temp)==k:
#             last=temp[-1]
#             first=temp[0]
#             ans=min(ans,last-first)
# print(ans)  


# n=9
# ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
# dict={}
# for i in ar:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# pairs=0
# for i in dict.values():
#         pairs=pairs+i//2
#     # pairs+=i//2
# print(pairs)                
# def traling_zeros(n):
#     res=0
#     powerof5=5
#     while n>=powerof5:
#         res=res+(n//powerof5)
#         powerof5=powerof5*5
#     return res
# n=int(input("enter nmbr:"))   
# ans=traling_zeros(n)
# print(ans)

# def lcm(a,b):
#     res=max(a,b)
#     while(True):
#         if(res%a==0 and res%b==0):
#             break
#         res=res+1
#     return res
# a=7
# b=3
# ans=lcm(a,b)
# print(ans)                 

# def traling_zeros(n):
#     res=0
#     powerof5=5
#     while n>=powerof5:
#         res=res+(n//powerof5)
#         powerof5=powerof5*5
#     return res
# n=int(input("enter nmbr:"))   
# ans=traling_zeros(n)
# print(ans)

# a=[5,6,7]
# b=[3,6,10]
# a_point=0
# b_point=0
# for a,b in zip(a,b):
#     if a>b:
#         a_point+=1
#     elif a==b:
#         a_point==b_point
#     else:
#         b_point+=1            
# print(a_point,b_point)


# a=[5,6,7]
# b=[3,6,10]
# a_points=0
# b_points=0
# for a,b in zip(a,b):
#     if a>b:
#         a_points+=1
#     elif a==b:
#         a_points==b_points    
#     else:
#         b_points+=1    
# print(a_points,b_points)

# [print(i) for i in range(5)]

# evens = [i for i in range(10) if i % 2 == 0]
# print(evens)

# evn=[i for i in range(10) if i%2!=0]
# print(evn)
# list=["even" if x%2==0 else "odd" for x in range(6)]

# s="   fly me   to   the moon  "
# n=len(s)
# current_len=0
# i=n-1
# while i>0 and s[i]==" ":
#     i-=1
# while i>0 and s[i]!=" ":
#     current_len+=1
#     i-=1
# print(current_len)      
# 
# li=[10,20,30,45,67,8,9,67]
# for i in li:
#     print(i)

# for ch in range(ord('a'),ord('z')):
#     print(chr(ch),":",ch)

# s="3902"
# new_s = ""
# for i in range(len(s) - 1):
#     a = int(s[i])
#     b = int(s[i + 1])
#     total = (a + b) % 10
#     new_s += str(total)
# print(new_s)    

# s= "aaaaabbc"
# dict={}
# for char in s:
#     if char in dict:
#         dict[char]+=1
#     else:
#         dict[char]=1
# odd_count=[]
# even_count=[]
# for i in  dict.values():
#     if i%2==0:
#         even_count.append(i)
#     else:
#         odd_count.append(i)  
# max_dif=float("-inf")
# for odd in odd_count:
#     for even in even_count:
#         max_dif=max(max_dif,odd-even)          
# print(max_dif)

# s="24123"
# odd_sum=0
# even_sum=0
# for i in range(0,len(s),2):
#     odd_sum+=int(s[i])
# for i in range(1,len(s),2):
#     even_sum+=int(s[i])    
# if odd_sum==even_sum:
#     print("True")
# else:
#     print("False")        
# # print(odd_sum)
# # print(even_sum)/

# nums=[2,7,11,15]
# target=9
# n=len(nums)
# res=[]
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             res=[i,j]
#             break
# print(res)        
# nums=[4,3,2,7,8,2,3,1]
# n=len(nums)
# actual_sum=0
# temp_sum=0
# for i in nums:
#     temp_sum+=i
# for i in range(n+1):
#     actual_sum+=i
# print(temp_sum) 
# print(actual_sum)   
# print(actual_sum-temp_sum)  

# nums=[1,1]
# n=len(nums)
# temp=[]
# for i in range(1,n+1):
#     if i not in nums:
#         temp.append(i)
# print(temp)
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# res=[]
# for i in list1:
#     for j in list2:
#         if list1[i]==list2[j]:
#             res.append(i,j)
# print(res)            

# n=5
# arr=[]
# for i in range(n):
#     n=int(input("enter nmbr:"))
#     arr.append(n)
#     arr.append(11)
# print(arr)    


