print("======Bilangan Faktorial======")
print()
def faktorial(x):
    if x == 1:
        return 1
    else:
        return(x* faktorial(x-1))

bil = int(input("Masukkan angka : "))
print("Faktorial dari bil", bil , "adalah" , faktorial(bil))

print()

