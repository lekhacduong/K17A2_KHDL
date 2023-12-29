def sign(x):
    if x < 0:
        x= "-1"
    elif x > 0:
        x= "1"
    else:
        x= "0"
    return x

print(sign(8))
print(sign(-8))
print(sign(0))