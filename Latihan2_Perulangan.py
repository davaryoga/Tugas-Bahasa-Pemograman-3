print("=======================================")
print("   Muhammad Dava Aryoga (312110552)")
print(" Program Bilangan Acak Kurang Dari 0,5")
print("=======================================")

from random import random
n = int(input("Masukan Jumlah Bilangan :"))
for i in range(n):
        bil = random()%0.5
        print(bil)
