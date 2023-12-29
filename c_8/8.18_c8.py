import math
a=int(input("nhap mot so nguyen :"))
#kiem tra xem lon hon 1 hay khong
if a > 1:
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0 :
            print(a,"khong la so nguyen to")
            break
        else:
            print(a,"la so nguyen to")
else:
    print(a,"khong la so nguyen to")            
    