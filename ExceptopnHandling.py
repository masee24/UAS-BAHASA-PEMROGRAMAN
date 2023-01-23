try:
    r = int(input('masukkan nilai r '))
    s = int(input('masukkan nilai s '))
    print('hasil a/b adalah',r/s)
except ZeroDivisionError:
    print('masukkan angka selain 0')