nama = input('Masukkan nama mahasiswa : ')
nim = input('Masukkan NIM-nya : ')

if nim[0:2] == '71' and 20 <= int(nim[2:4]) <= 22:
    print(nama, 'merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print(nama, 'bukan mahasiswa informatika angkatan 20 hingga 22')
