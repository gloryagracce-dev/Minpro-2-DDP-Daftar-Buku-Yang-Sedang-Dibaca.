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

1). Mulai

program dimulai dari bentuk elif, lalu lanjutkan ke langkah berikutnya.

2). Masukkan Data (login)

pengguna dimminta mengidentifikasi nama dan sandi. ini tempat memasukkan data.

3). Cek nama & sandi

program memriksa: "apakah nama & sandi yang dimasukkan benar?"

- Jika TIDAK, Muncul tulisan "Nama atau sandi salah!", lalu kembali ke awal untuk memasukkan nama lagi.

- Jika YA, Muncul tulisan "Berhasil masuk!", lalu lanjut ke langkah berikutnya.

4). Cek peran Pengguna

  program menanyakan: "Peran Siapa?"

- ADMIN, Masuk ke Menu Admin, isinya 5 pilihan:

    1. Tambah buku
   
    2. Lihat semua buku
   
    3. Ubah data buku
   
    4. Hapus buku
   
    5. Keluar
   
    setelah selesai memilih dan melakukan sesuatu, bisa kembali ke menu. Kalau pilih Keluar, program berhenti di [Selesai].

- PEMBACA, Masuk ke Menu Pembaca, isinya cuma 2 pilihan:

  1. Lihat semua buku
 
  2. Keluar

  Tidak bisa menambah, mengubah, atau menghapus. Kalau pilih Keluar, program berhenti di [Selesai].

5). Selesai

  Program berakhir dan berhenti berjalan.


3. DOKUMENTASI PROGRAM & OUTPUT


ADMIN:


   <img width="960" height="600" alt="Screenshot 2026-10-04 210838" src="https://github.com/user-attachments/assets/3565aad4-5acc-4cdb-935c-bdced7ea38b6" />

   <img width="960" height="600" alt="Screenshot 2026-10-04 210854" src="https://github.com/user-attachments/assets/7d0694d7-2d45-49e0-8edc-41bf8b1c8fdd" />

   <img width="960" height="600" alt="Screenshot 2026-10-04 210909" src="https://github.com/user-attachments/assets/9efaad4a-1ef2-4715-9efb-175e950e17c1" />


PENGGUNA: 


   <img width="960" height="600" alt="Screenshot 2026-10-04 211059" src="https://github.com/user-attachments/assets/4adef348-1169-49f6-9cf3-72da4ca255f1" />
