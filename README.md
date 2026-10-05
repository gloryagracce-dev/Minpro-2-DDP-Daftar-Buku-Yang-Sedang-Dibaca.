# Minpro-2-DDP-Daftar-Buku-Yang-Sedang-Dibaca.

Nama: Graceilla Tifunny Glory Hutagalung

NIM: 079

Kelas: B

1. PENJELASAN MENGENAI KODE:

- Import time:
  
  Time buat memberi jeda tampilan agar mudah dibaca

- Datetime:

  Menampilkan tanggal dan waktu saat login

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

program ini berfungsi untuk mengelola data buku perpustakaan sederhana. Terdapat sistem masuk dengan dua jenis pengguna: 

Admin: yang bisa menambah, melihat, mengubah, dan menhapus data buku, serta

pengguna biasa: yang hanya bisa melihat daftar buku. Data disimpan menggunakan Dictionary python.


2. GAMBAR FLOWCHART:

  <img width="1026" height="1540" alt="Flowchart Daftar buku drawio (2)" src="https://github.com/user-attachments/assets/565e9281-c81a-411b-b6e0-932d68a40c0f" />

 
PENJELASAN ALUR FLOWCHART:

1. TITIK AWAL & PENENTUAN PERAN (USER ROLE):

​START: Menandai dimulainya program sistem.
  
​User Role?: Sistem melakukan pengecekan peran pengguna.

Logika bercabang menjadi dua:  

​1). Admin: Pengguna masuk ke menu utama Admin yang memiliki akses penuh (Tambah, Lihat, Ubah, Hapus, Keluar).  

​2). Pengguna: Pengguna masuk ke menu khusus yang hanya memiliki akses terbatas (Lihat Semua Buku & Keluar).  

​2. ALUR KERJA ADMIN:

​Setelah memilih opsi menu (angka 1–5), sistem menjalankan alur sesuai pilihan:  

​1). Tambah Buku:
​Sistem meminta input Nama Buku dan Halaman Terakhir Dibaca.  

​Sistem menjalankan proses internal Simpan data ke daftar.  

​Sistem menampilkan pesan Berhasil ditambahkan, lalu garis panah mengarahkan alur kembali ke Tampil Menu Admin.  

​2). Lihat Semua Buku:

​Sistem mengecek Cek apakah ada data?

​Jika Ya, sistem menampilkan Tampil semua daftar.

​Jika Tidak, sistem menampilkan Tampil "Belum ada data".

​Alur kembali ke Tampil Menu Admin.

​3). Ubah Data Buku:

​Sistem mengecek ketersediaan data buku. Jika kosong, tampil Belum ada data.

​Jika ada data, sistem meminta input Masukkan nomor yang diubah.  

​Sistem mengecek Cek nomor ada?. Jika tidak ada, tampil Nomor tidak ada.  
​Jika nomor valid (Ya), sistem meminta input Nama baru dan Halaman baru, lalu memproses Ganti data lama dengan yang baru.  
​Setelah tampil Berhasil diubah, alur kembali ke Tampil Menu Admin.  

​4). Hapus Buku:

​Sistem mengecek ketersediaan data. Jika kosong, tampil Belum ada data.  
​Jika ada data, sistem meminta input Masukkan nomor yang dihapus.  
​Sistem mengecek validitas nomor. Jika nomor ada (Ya), sistem memproses Hapus data dari daftar.  
​Setelah tampil Berhasil dihapus, alur kembali ke Tampil Menu Admin.  

​5). Keluar:

​Sistem menampilkan pesan Program selesai dan alur menuju ke titik END (program berhenti).

3. ALUR KERJA PERAN PENGGUNA (USER):

​Pengguna hanya disajikan 2 pilihan menu:  

​1).  Lihat Semua Buku:

​Sama seperti fungsi milik Admin, sistem mengecek ketersediaan data. Jika ada, data ditampilkan; jika tidak ada, tampil pesan Belum ada data. Setelah itu alur kembali ke Menu Pengguna.  

​2). Keluar:

​Sistem menampilkan pesan Program selesai dan alur berakhir di END

3. DOKUMENTASI PROGRAM & OUTPUT


ADMIN:


   <img width="960" height="600" alt="Screenshot 2026-10-04 210838" src="https://github.com/user-attachments/assets/3565aad4-5acc-4cdb-935c-bdced7ea38b6" />

   <img width="960" height="600" alt="Screenshot 2026-10-04 210854" src="https://github.com/user-attachments/assets/7d0694d7-2d45-49e0-8edc-41bf8b1c8fdd" />

   <img width="960" height="600" alt="Screenshot 2026-10-04 210909" src="https://github.com/user-attachments/assets/9efaad4a-1ef2-4715-9efb-175e950e17c1" />


PENGGUNA: 


   <img width="960" height="600" alt="Screenshot 2026-10-04 211059" src="https://github.com/user-attachments/assets/4adef348-1169-49f6-9cf3-72da4ca255f1" />
