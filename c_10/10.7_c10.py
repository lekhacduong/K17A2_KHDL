s = input("Nhập chuỗi s: ")
s_sub = input("Nhập chuỗi s_sub: ")
s_find = input("Nhập chuỗi tìm s_find: ")
s_replace = input("Nhập chuỗi thay thế s_replace: ")
#loại bỏ khoảng trắng ở đầu và cuối chuỗi:
s.strip()
print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi: ",s.strip())
#số lần s_sub xuất hiện trong s:
s.count(s_sub)
print("Số lần s_sub xuất hiện trong s: ",s.count(s_sub))


#chuỗi s sau khi tìm và thay thế:
s.replace(s_find,s_replace)
print("Chuỗi s sau khi tìm kiếm và thay thế là: ",s.replace(s_find,s_replace))