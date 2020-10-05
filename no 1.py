#Mengubah meter menjadi konversi panjang yang lain
x = str(input("Masukkan konversi: "))
m = int(input("Masukkan berapa meter: "))
if x == "km":
    print("meter menjadi km = ", m/1000, x)
elif x == "hm":
    print("m menjadi hm = ", m/100, x)
elif x == "dam":
    print("m menjadi dam = ", m/10, x)
elif x == "m":
    print("m = ", m,x)
elif x == "dm":
    print("m menjadi dm = :", m*10, x)
elif x == "cm":
    print("m menjadi cm = :", m*100, x)
elif x == "mm" :
    print("m menjadi mm = :", m*100, x)
