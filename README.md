# Tugas-Bahasa-Pemograman-3
```
Nama  : Muhammad Dava Aryoga
NIM   : 312110552
Kelas : TI.21.C.3
Prodi : Teknik Informatika
```
## Latihan1_Struktur_Kondisi.py
```
print('======================================')
print('   Muhammad Dava Aryoga (312110552)')
print(' Program Menentukan Bilangan Terbesar')
print('======================================')
a = int(input("Masukan bilangan pertama   : "))
b = int(input("Masukan bilangan kedua     : "))
 
if a > b:
    maks = a
else:
    maks = b
print('Nilai Terbesar adalah      : %d' % maks)
```

### Penjelasan Program
1. Pertama kita berikan perintah `input` nilai bialangan pertama dan kedua
```
a = int(input("Masukan bilangan pertama   : "))
b = int(input("Masukan bilangan kedua     : "))
```

2. Lalu kita gunakan fungsi `if` dan `else` untuk menentukan bilangan terbesar
```
if a > b:
    maks = a
else:
    maks = b
```

3. Kemudian gunakan perintah `print` untuk menampilkan bilangan terbesar 
```
print('Nilai Terbesar adalah      : %d' % maks)
```

4. Keitka di eksekusi kita akan di perintahkan untuk memasukan nilai bilangan pertama

![Screenshot (55)](https://user-images.githubusercontent.com/92939686/142245894-c7282b39-218e-46f0-9a30-b014f23c8d1a.png)

5. Dilanjiutkan dengan bilangan kedua

![Screenshot (56)](https://user-images.githubusercontent.com/92939686/142245989-992f7c05-c3e6-455f-aac0-89c60a796b21.png)

6. Lalu akan dihasilkan output terakhir seperti ini

![Screenshot (52)](https://user-images.githubusercontent.com/92939686/142244213-9c11fc21-3867-417a-841f-675d96db938f.png)

## Latihan2_Struktur_Kondisi.py
```
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
```

### Penjelasan Program
1. Pertama kita gunakan perintah `input` untuk memasukan nilai bilangan pertama, kedua, dan ketiga
```
a = int(input("Masukkan Bilangan Pertama  : "))
b = int(input("Masukkan Bilangan Kedua    : "))
c = int(input("Masukkan Bilangan Ketiga   : "))
```

2. Kemudian gunakan fungsi `if` dan `eilf` untuk menentukan dan mengurutkan dari bilangan yang terkecil ke terbesar, lalu sekaligus gunakan perintah `print` untuk         menampilkan urutan bilangan

```
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
```

3. Ketika di eksekusi kita akan diperintahkan untuk memasukan bilangan pertama, kedua, dan ketiga

![Screenshot (61)](https://user-images.githubusercontent.com/92939686/142248129-324172c3-970b-466e-9ef0-41afab388215.png)

![Screenshot (62)](https://user-images.githubusercontent.com/92939686/142248162-ce3208c1-7e36-4fac-a35a-3d27733e9d5f.png)

![Screenshot (63)](https://user-images.githubusercontent.com/92939686/142248185-a8825ea9-24b9-421e-9ca5-2ec3374fe677.png)

4. Lalu hasil output akhir akan ditampilkan sebagai berikut

![Screenshot (64)](https://user-images.githubusercontent.com/92939686/142248300-e305be55-645f-4e69-8dc1-aef56efb065c.png)

## Latihan1_Perulangan.py
```
print("====================================")
print("  Muhammad Dava Aryoga (312110552)")
print("    Program Bilangan Bertingkat")
print("====================================")

for i in range(10):
    for j in range(10):
       print('%2d'%(i + j), end=' ')
    print()
```

### Penjelasan Program
1. Pertama kita gunakan perulangan `for` pada variabel `i`dan`j`, lalu untuk memberikan jarak gunakan `range`
```
for i in range(10):
    for j in range(10):
```

2. Kemudian gunakan perintah `print` untuk menampilkan output
```
print('%2d'%(i + j), end=' ')
    print()
```

3. Lalu output akan ditampilkan sebagai berikut

![Screenshot (67)](https://user-images.githubusercontent.com/92939686/142260612-7b80f65c-6a72-45df-81bc-4a83aff705b2.png)

## Latihan2_Perulangan.py
```
print("=======================================")
print("   Muhammad Dava Aryoga (312110552)")
print(" Program Bilangan Acak Kurang Dari 0,5")
print("=======================================")

from random import random
n = int(input("Masukan Jumlah Bilangan :"))
for i in range(n):
        bil = random()%0.5
        print(bil)
```

### Penjelasan Program
1. Pertama kita menggunakan `from` pada `random` dan kita `import` `random`, untuk mendeklarasikan nilai random
```
from random import random
```

2. Lalu kita deklarasikan nilai `n` sebagai `int` dan lakukan perintah `input` untuk memasukan nilai
```
n = int(input("Masukan Jumlah Bilangan :"))
```

3. Lalu gunakan `for` pada variabel `i` dan gunakan `in range` untuk memberikan limit/jarak, limit tersebut adalah `0.5`
```
for i in range(n):
        bil = random()%0.5
```

4. Kemudian gunakan perintah `print` untuk menampilkan hasil/output
```
 print(bil)
```

5. Jika kita eksekusi, kita akan diperintahkan untuk memasukan nilai

![Screenshot (70)](https://user-images.githubusercontent.com/92939686/142262088-f42edb2d-47bd-46da-a695-5cb10bc66df7.png)

6. Misalkan kita input 5, maka hasil/output akan ditampilkan sebagai berikut

![Screenshot (71)](https://user-images.githubusercontent.com/92939686/142262209-058f0723-2306-4df1-b36b-148dc0394f77.png)

## Sekian Terima Kasih




