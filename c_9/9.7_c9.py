def phep_chia(x,y):
    phan_nguyen= x // y
    return phan_nguyen

x=int(input("Nhap so chia :"))
y=int(input("Nhap so bi chia :"))
print(f"Phan nguyen cua {x} chia {y} la : {phep_chia(x,y)}")