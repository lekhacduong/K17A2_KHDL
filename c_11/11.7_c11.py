L = [1,2,3,4]
thresh = 2
a=[]
def elementwise_greater_than(L,thresh):
   for i in L:
       if i <= thresh:
            b=False
            a.append(b)
       if i > thresh:
                b=True
                a.append(b)
   return a
print(elementwise_greater_than(L,thresh))
             
    