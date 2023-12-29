def tinh_S(n,x):
    S=((x**2)+1)**n
    return S

n=int(input("nhap n :")) 
x=int(input("nhap x :"))
print(f"S co gia tri la :{tinh_S(n,x)}")