# Minpro-2-DDP-Daftar-Buku-Yang-Sedang-Dibaca.

Nama: Graceilla Tifunny Glory Hutagalung

NIM: 079

Kelas: B

1. PENJELASAN MENGENAI KODE:

- Import time & from datetime import datetime ini Library yang dipakai:
  
  Time buat jeda sebentar agar tidak langsung lewat, datetime buat tampilin tanggal waktu sekarang.

- Pengguna = {...}:

  tempat simpan daftar siapa yang boleh masuk, ada nama, sandi, dan perannya (admin atau user).

- Perpustakaan = {}:

  ini tempat simpan semua data buku pakai Dictionary, jadi tiap judul ada isinya penulis dan tahun.

- def login():

  fungsi cek nama dan sandi, Kalau bener, kasih tau perannya. Kalau salah, kasih pesan gagal.

- def tambah_buku():

  fungsi masukin buku baru ke dalam daftar.

- def tampil_buku():

  fungsi keluarin semua buku yang sudah di simpan, biar gampang dibaca.

- def ubah_buku():

  fungsi ganti data buku yang sudah ada.

- def hapus_buku():

  fungsi buang buku dari daftar.

- menu_admin():

  tampilkan pilihan lengkap: taambah, lihat, ubah, hapus, keluar.

- menu_user():

  tampilkan pilihan terbatas: cuma bisa lihat buku, tapi gak bisa ubah/hapus.

- if_nama_ == "_main_":

  tempat jalan program dari awal. Tampil tanggal, minta login, lalu masuk ke menu sesuai peran.



- 
