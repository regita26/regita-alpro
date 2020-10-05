#list mula-mula
buah = ["jeruk", "apel", "mangga", "durian"]
buah.insert(2,"leci")
print(buah)

#membuat list kosong untu menampung hobi
hobi = []
stop = False
i = 0

#mengisi hobi
while(not stop) :
    hobi_baru = raw_input("inputkan hobi yang ke-{}: ".format(i))
    hobi.append(hobi_baru)

    #incremet i
    i += 1

    tanya = raw_input("Mau isi lagi? (y/t): ")
    if (tanya == "t"):
        stop = True
#cetak semua hobi
print "Kamu memiliki {} hobi.format(len(hobi))
for hb in hobi :
    print "- {".format(hb)


