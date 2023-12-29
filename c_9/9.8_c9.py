def so_hoan_hao(x):
    if x <=0:
        return False
    tong=0
    for i in range(1,x):
        if x % i ==0:
            tong+=i
            if tong == x:
                return True

x=int(input("Nhap so nguyen x de kiem tra so hoan hao :")) 
if so_hoan_hao(x):
    print(f"{x} la so hoan hao.")
else:
    print(f"{x} Khong phai so hoan hao.")
                