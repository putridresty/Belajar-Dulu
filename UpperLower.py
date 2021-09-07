kalimat = input('Masukkan Kalimat: ')
HurufBesar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
HurufKecil = 'abcdefghijklmnopqrstuvwxyz'
bilangan = '1234567890'

kapital = []
kecil = []
angka = []
potongan = kalimat.split()

for karakter in kalimat :
    if karakter in HurufBesar:
        kapital += karakter
    elif karakter in HurufKecil:
        kecil += karakter
    elif karakter in bilangan:
        angka += karakter

print('Jumlah total angka adalah: '+str(len(angka)))
print('Jumlah total kata adalah: '+str(len(potongan)))
print('Jumlah total huruf kapital adalah: '+str(len(kapital)))
print('Jumlah total huruf kecil adalah: '+str(len(kecil)))