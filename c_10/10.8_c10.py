from datetime import datetime
import time
import calendar
ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
ngay_thang_nam=datetime(nam,thang,ngay)
print("Ngày tháng năm vừa nhập là: ",ngay_thang_nam.strftime("%d-%m-%Y"))

#ktra xem phai nam nhuan hay khong:
calendar.isleap(nam)
if calendar.isleap == True:
    print(f"Năm {nam} là năm nhuận ")
else:
    print(f"Năm {nam} không là năm nhuận")
    
#kiem tra xem ngày thang nam nhập vào là thứ mấy :
calendar.weekday(nam,thang,ngay)
if calendar.weekday(nam,thang,ngay) == 0:
    print(f"{ngay} - {thang} - {nam} là Thứ Hai")
elif calendar.weekday(nam,thang,ngay) == 1:
    print(f"{ngay} - {thang} - {nam} là Thứ Ba")
elif calendar.weekday(nam,thang,ngay) == 2:
    print(f"{ngay} - {thang} - {nam} là Thứ Tư")
elif calendar.weekday(nam,thang,ngay) == 3:
    print(f"{ngay} - {thang} - {nam} là Thứ Năm")
elif calendar.weekday(nam,thang,ngay) == 4:
    print(f"{ngay} - {thang} - {nam} là Thứ Sáu")
elif calendar.weekday(nam,thang,ngay) == 5:
    print(f"{ngay} - {thang} - {nam} là Thứ Bảy")
else:
    print(f"{ngay} - {thang} - {nam} là Chủ Nhật")
    
#cho biết tháng nhập vào có bn ngày:
so_ngay = calendar.monthrange(nam, thang)[1]
print(f"Số ngày trong tháng {thang} là: {so_ngay}")
    