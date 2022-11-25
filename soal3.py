n1 = int(input('Masukkan nilai soal 1: '))
n2 = int(input('Masukkan nilai soal 2: '))
n3 = int(input('Masukkan nilai soal 3: '))
umur = int(input('Masukkan umur Anda: '))
rata = (n1*0.5) + (n2*0.3) + (n3*0.2)
print('Rata-rata nilai Anda:', rata)

if rata >= 80 and umur <= 25:
    print('Selamat Anda lulus!')
elif umur > 25 and rata >= 90:
    print('Selamat Anda lulus!')
else:
    print('Coba lagi tahun depan!')
