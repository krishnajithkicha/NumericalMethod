def Add():
    mat1=[]
    mat2=[]
    rows1=int(input("Enter the no of rows:"))
    cols1=int(input("Enter the no of cols:"))
    for i in range(rows1):
        rows=[]
        print("Enter the rows of first matrix:")
        for j in range(cols1):
            num=int(input())
            rows.append(num)
        mat1.append(rows)
    rows2=int(input("Enter the no of rows:"))
    cols2=int(input("Enter the no of cols:"))
    for i in range(rows2):
        rowss=[]
        print("Enter the rows of second matrix:")
        for j in range(cols2):
            nums=int(input())
            rowss.append(nums)
        mat2.append(rows)
    print(mat1)
    print(mat2)
    print("Addition of matrix")
    if(rows1!=rows2 or cols1!=cols2):
        print("Invalid format")
    else:
        sum=[]
        for i in range(rows1):
            rowsum=[]
            for j in range(cols1):
                add=mat1[i][j]+mat2[i][j]
                rowsum.append(add)
            sum.append(rowsum)
    return sum
sum=Add()
print("Sum",sum)
    
