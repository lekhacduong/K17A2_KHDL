def tinh_A(n,x):
    A=(x**2 + x + 1)**n + (x**2 - x +1)**n
    return A


print(tinh_A(2,3))