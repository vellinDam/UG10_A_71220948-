print('==== Selamat datang di Toko Andi Tersenyum, selamat berbelanja! ====')
total = int(input('Total belanja: Rp.'))

if total >= 1000000:
    diskon = 0.1
elif total >= 500000:
    diskon = 0.05
elif total >= 100000:
    diskon = 0.02
else:
    diskon = 0

total -= (total * diskon)
if diskon == 0:
    print('Tidak ada diskon! Maka yang Anda bayarkan adalah: Rp.', total)
else:
    print('Biaya yang hharus dibayar setelah diskon adalah: Rp.', total)
