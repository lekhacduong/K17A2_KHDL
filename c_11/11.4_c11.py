#giá trị các phần tử tỏng líst a:
a=[]
while True:
    m=int(input("Nhập giá trị:       "))
    a.append(m)
    n=int(input("Tiếp tục nhập giá trị?   1:Có   0:Không          "))
    if n == 1:
        continue
    else:
        break
    
#nhập x:
x=int(input("Nhập giá trị cần tìm x:   "))
#xuất list:
print("List:  ",a)
#tổng list:
tong=sum(a)
print("Tổng các giá trị trong list:   ",tong)
print(x," xuất hiện ",a.count(x)," lần trong list")
b=[]
for i in a:
    if i > 5:
        b.append(i)
    
print("Các số lớn hơn",x,"trong list: ",b)
