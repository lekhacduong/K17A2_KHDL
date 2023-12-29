import math

#ax^2+bx+c
def giai_pt_bac2(a,b,c):
    if a == 0:
        print(f"{b}x+{c}=0")
        return True
    else:
        print(f"{a}x^2+{b}x+{c}=0")
        return False
    
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
x=-c/b
if giai_pt_bac2(a,b,c):
    print(f"Phương trình có nghiệm x={x}")
else:
    delta = pow(b,2) - 4 * a * c
    if delta == 0:
        print(f"Phương trình có nghiệm duy nhất x={x}")
    elif delta < 0:
        print("Phương trình vô nghiệm")
    else:
        x1 = ((- b - (math.sqrt(delta))) / 2 * a)
        x2 = ((- b + (math.sqrt(delta))) / 2 * a)
        print(f"Phương trình có nghiệm x1={x1}   x2={x2}")