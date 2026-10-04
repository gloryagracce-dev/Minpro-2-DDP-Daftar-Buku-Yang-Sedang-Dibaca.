import time
from datetime import datetime
# === DATA PENGGUNA - BARU DITAMBAH ===
pengguna = {
    "admin": {"sandi":"1234","peran": "admin"},
    "pembaca": {"sandi":"4567","peran":"pembaca"}
}
daftar_buku = []
# === FUNGSI LOGIN - BARU DITAMBAH ===
def login():
    print("\n=== MASUK AKUN ===")
    while True:
        try:
            nama = input("Nama: ")
            sandi = input("Sandi: ")

            if not nama or not sandi:
                print("Nama dan Sandi tidak boleh kosong!")
                time.sleep(0.5)
                continue
            if nama in pengguna and pengguna[nama]["sandi"] == sandi:
                print(f"Berhasil masuk! Halo {nama}")
                time.sleep(1)
                return pengguna[nama]["peran"]
            else:
                print("Nama atau sandi salah! Coba lagi.")
                time.sleep(0.8)
        except:
            print("Terjadi kesalahan!")
            continue
# === MENU ADMIN - AKSEES LENGKAP ===
def menu_admin():
    while True:
         print("\n===== MENU DAFTAR BUKU =====")
         print("1. Tambah Buku")
         print("2. Lihat Semua Buku")
         print("3. Ubah Data Buku")
         print("4. Hapus Buku")
         print("5. Keluar")
         pilihan = input("Masukkan pilihan angka [1-5]: ")
         if pilihan not in ["1", "2", "3", "4", "5",]:
             print("Pilihan tidak ada! Coba lagi.")
             continue

         if pilihan == "1":
            nama = input("Masukkan nama buku: ")
            try:
                hal = int(input("Masukkan halaman terakhir dibaca: "))
            except:
               print("Halaman harus berupa angka!")
               continue
            daftar_buku.append({"judul": nama, "halaman": hal})
            print("Berhasil ditambahkan!")

         elif pilihan == "2":
             if len(daftar_buku) == 0:
                 print("Belum ada catatan buku.")
             else:
                 print("\n--- DAFTAR BUKU ---")
                 for i, buku in enumerate(daftar_buku, start=1):
                     print(f"{i}. judul: {buku['judul']} | halaman: {buku['halaman']}")

         elif pilihan == "3":
             if len(daftar_buku) == 0:
                 print("Belum ada data buku.")
             else:
                 try:
                     nomor = int(input("Masukkan nomor buku yang mau diubah: ")) - 1
                 except:
                     print("Harus masukkan angka!")
                     continue
                 if 0 <= nomor < len(daftar_buku):
                     nama_baru = input("Masukkan judul baru: ")
                     try:
                         hal_baru = int(input("Masukkan halaman baru: "))
                     except:
                         print("Halaman harus berupa angka!")
                         continue
                     daftar_buku[nomor] = {" Judul": nama_baru, "Halaman": hal_baru}
                     print("Berhasil diubah!")
                 else:
                     print("Nomor buku tidak ada!")
    
         elif pilihan == "4":
            if len(daftar_buku) == 0:
                print("Belum ada data buku.")
            else:
                try:
                    nomor = int(input("Masukkan nomor buku yang mau dihapus: ")) - 1
                except:
                    print("Harus masukkan angka!")
                    continue
                if 0 <= nomor < len(daftar_buku):
                     daftar_buku.pop(nomor)
                     print("Berhasil dihapus!")
                else:
                     print("Nomor buku tidak ada!")

         elif pilihan == "5":
             print("Program selesai, Terima Kasih!")
             break
# ==== MENU PENGGUNA - HANYA LIHAT ===
def menu_pengguna():
    while True:
        print("\n===== MENU =====")
        print("1. Lihat Semua Buku")
        print("2. Keluar")

        pilihan = input("Masukkan pilihan angka [1-2]: ")

        if pilihan == "1":
            if len(daftar_buku) == 0:
                print("Belum ada catatan buku.")
            else:
                print("\n--- DAFTAR BUKU ---")
                for i, buku in enumerate(daftar_buku, start=1):
                    print(f"{i}. Judul: {buku['judul']} | Halaman: {buku['halaman']}")
        elif pilihan == "2":
            print("Program selesai, Terima Kasih!")
            break
        else:
            print("Pilihan tidak ada! Coba lagi.")
# === JALANKAN PROGRAM ===
akun = ""
while akun == "":
    akun = login()
if akun == "admin":
    menu_admin()
elif akun == "pembaca":
    menu_pengguna()
else:
    print("Akses ditolak!")