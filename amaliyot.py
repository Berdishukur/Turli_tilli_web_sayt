
kiyimlar=["Mayka","Shim","ko'ylak","kurutka","Paypoq","Kepka"]
new_clothes=[]
i=0
while i<len(kiyimlar):
    if kiyimlar[i].lower().startswith("k"):
        new_clothes.append(kiyimlar[i])
    i+=1
print(new_clothes)