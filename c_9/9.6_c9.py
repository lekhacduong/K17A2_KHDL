def kiem_tra_so_nguyen_to(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

so_nguyen_to=int(input("nhap mot so :"))   
if kiem_tra_so_nguyen_to(so_nguyen_to):
    print(f"{so_nguyen_to} la so nguyen to")
else:
    print(f"{so_nguyen_to} khong la so nguyen to")  