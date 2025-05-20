# Print a matrix
def matrix_arrays(matrix):
    for column in matrix:
        print(column)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix_arrays(matrix)        

# create and print a matrix
def print_matrix(matrix):
    for row in matrix:
        for ele in row:
            print(ele,end=" ")
        print()    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)

# MATRIX ADDITION
# MATRIX ADDITION
def add(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    return result
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,4,5],[9,8,7],[7,2,9]]
res=add(A,B)
print(res,end="")
# MATRIX ADDITION
def add(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    return result
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,4,5],[9,8,7],[7,2,9]]
res=add(A,B)
for row in res:
    print(row)
# MATRIX SUBTRACTION
def add(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]-B[i][j])
        result.append(row)
    return result
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,4,5],[9,8,7],[7,2,9]]
res=add(A,B)
for row in res:
    print(row)



