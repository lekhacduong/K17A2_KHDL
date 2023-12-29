# ham ghi de vao cuoi tep
def write_end_of_file(file_name,content):
    with open(file_name, 'a') as f:
        f.write(content + '\n')
        f.close()

# ham doc tap tin
def read_file(file_name):
    with open(file_name, 'r') as f:
        a = f.read()
        f.close()
        return a

# xu li vong lap        
f = input("Nhap ten tap tin: ")
while True:
    m = input("Nhap noi dung: ")
    write_end_of_file(f,m)
    n = int(input("Ban co muon tiep tuc ghi noi dung vao file?   1:Co    0:Khong   "))
    if n == 1:
        continue
    else:
        break
    
# xuat
print("Da ghi noi dung vao tap tin",f)
print(read_file(f))