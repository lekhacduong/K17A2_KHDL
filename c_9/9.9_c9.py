import math
r=int(input("Nhap ban kinh :"))
a=int(input("Nhap chieu dai :"))
b=int(input("Nhap chieu rong :"))
chu_vi_circle = lambda r: 2*r*math.pi
print("Chu vi hinh tron co ban kinh ",r," la : ",chu_vi_circle(r))
dien_tich_circle = lambda r: math.pi*(r**2)
print("Dien tich hinh tron co ban kinh ",r,"la : ",dien_tich_circle(r))
chu_vi_rectangle = lambda a, b: (a+b)*2
print("Chu vi hinh chu nhat co chieu dai ",a," va chieu rong ",b," la : ",chu_vi_rectangle(a,b))
dien_tich_rectangle = lambda a, b: a*b
print("dien tich hinh chu nhat co chieu dai ",a," va chieu rong ",b," la : ",dien_tich_rectangle(a,b))
