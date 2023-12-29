def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/(chieu_cao*chieu_cao)
    if bmi < 18.5:
        chi_so='Gay'
    elif bmi >=18.5 and bmi <=24.99:
        chi_so='Binh Thuong'
    else:
        chi_so='Thua Can'
    return chi_so

can_nang=float(input('nhap chi so can nang :'))
chieu_cao=float(input('nhap chi so chieu cao :'))
print(f"Ban bi :{tinh_bmi(can_nang,chieu_cao)}")





