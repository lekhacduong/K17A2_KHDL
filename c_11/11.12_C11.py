tuple_a = (3,1,2,4)
tuple_b = (5,7,6,8)
tuple_c = tuple_a + tuple_b
list_c = list(tuple_c)
list_c.sort()
tuple_d = tuple(list_c)
tuple_e = tuple_d[3]
tuple_f = tuple_d[-3:]



print("Tuple a:",tuple_a)
print("Tuple b:",tuple_b)
print("Tuple c:",tuple_c)
print("Tuple d:",tuple_d)
print("Tuple[3]",tuple_e)
print("3 phan tu cuoi cung cua tuple d:",tuple_f)