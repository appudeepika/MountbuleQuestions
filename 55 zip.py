a=[5,6,7]
b=[3,6,10]
a_points=0
b_points=0
for a,b in zip(a,b):
    if a>b:
        a_points+=1
    elif a==b:
        a_points==b_points    
    else:
        b_points+=1    
print(a_points,b_points)

a=[5,6,7]
b=[3,6,10]
for i in range(len(a)):
    print(a[i],b[i])