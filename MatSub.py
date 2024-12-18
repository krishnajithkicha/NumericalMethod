def Sub():
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
    print("Subtraction of matrix")
    d=[]
    for i in range(rows1):
        rowd=[]
        for j in range(cols1):
            d=mat1[i][j]-mat2[i][j]
            rowd.append(d)
        d.append(rowd)
    return d
D=Sub()
print("Diff",D)
    
