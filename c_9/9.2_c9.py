def tinh_can(nam):
    can=nam % 10
    if can == 0:
        nam_can='Canh'
    elif can == 1:
        nam_can='Tan'
    elif can ==2:
        nam_can='Nham'
    elif can ==3:
        nam_can='Quy'
    elif can ==4:
        nam_can='Giap'
    elif can ==5:
        nam_can='At'
    elif can ==6:
        nam_can='Binh'
    elif can ==7:
        nam_can='Dinh'
    elif can ==8:
        nam_can='Mau'
    else:
        nam_can='Ky'
    return nam_can


def tinh_chi(nam):
    chi=nam % 12
    if chi ==0:
        nam_chi='Than'
    elif chi ==1:
        nam_chi='Dau'
    elif chi ==2:
        nam_chi='Tuat'
    elif chi ==3:
        nam_chi='Hoi'
    elif chi ==4:
        nam_chi='Ty'
    elif chi ==5:
        nam_chi='Suu'
    elif chi ==6:
        nam_chi='Dan'
    elif chi ==7:
        nam_chi='Mao'
    elif chi ==8:
        nam_chi='Thin'
    elif chi ==9:
        nam_chi='Ty'
    elif chi ==10:
        nam_chi='Ngo'
    else:
        nam_chi='Mui'
    return nam_chi

nam=int(input("nhap nam :"))
print(f"Nam duong lich {nam} doi qua nam duong lich la :{tinh_can(nam)} {tinh_chi(nam)}")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    