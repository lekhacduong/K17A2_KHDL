a=[]
n=int(input("Nhap so luong so can tim min max :" ))
for i in range(n):
    m=int(input("Nhap so thu "+ str(i+1)+ ": "))
    a=a+[m]
print("Gia tri lon nhat la :",max(a))
print("Gia tri nho nhat la :",min(a))
    