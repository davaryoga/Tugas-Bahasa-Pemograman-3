print("====================================")
print("  Muhammad Dava Aryoga (312110552)")
print("     Program Mengurutkan Data")
print("====================================")

a = int(input("Masukkan Bilangan Pertama  : "))
b = int(input("Masukkan Bilangan Kedua    : "))
c = int(input("Masukkan Bilangan Ketiga   : "))

if a < b < c:
    print("Urutan Bilangan : %s" % a,b,c)
elif b < a < c:
    print("Urutan Bilangan : %s" % b,a,c)
elif a < c < b:
    print("Urutan Bilangan : %s" % a,c,b)
elif b < c < a:
    print("Urutan Bilangan : %s" % b,c,a)
elif c < a < b:
    print("Urutan Bilangan : %s" % c,a,b)
elif c < b < a:
    print("Urutan Bilangan : %s" % c,b,a)