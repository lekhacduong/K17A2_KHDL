
def kiem_tra_zipcode(ma_zip):
    if len(ma_zip) == 6:
        return True
    else:
        return False
    
ma_zip = input("Nhập mã zip: ")
if kiem_tra_zipcode(ma_zip):
    print("Mã zip hợp lệ")
else:
    print("Mã zip không hợp lệ")