list_animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animals: ",list_animals)
number_animals=len(list_animals)
print("Number of animals: ",number_animals)
x=input("Nhap ten dong vat can tim trong so thu: ")
search= x in list_animals
if x in list_animals:
    print(f"There is {x} in list of animals")
else:
    print(f"There isn't {x} in list of animals")