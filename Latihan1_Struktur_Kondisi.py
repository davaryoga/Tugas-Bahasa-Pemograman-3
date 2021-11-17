def main():
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
 
if __name__ == '__main__':
    main()