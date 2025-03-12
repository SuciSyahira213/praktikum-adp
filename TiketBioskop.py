daftar_film = {
    "01": ("Captain America", 55000),
    "02": ("Keluarga Cemara", 40000),
    "03": ("Avengers: Endgame", 75000),
    "04": ("Joker", 65000),
    "05": ("Frozen II", 50000)
}

print("Daftar Film yang Sedang Tayang:")
print ("----------------------------------------")
print ("| kode |    Nama Film       |    Harga  |")
print ("-----------------------------------------")
print ("|  01  | Captain America    | Rp.55.000 |")
print ("|  02  | Keluarga Cemara    | Rp.40.000 |")
print ("|  03  | Avengers: Endgame  | Rp.75.000 |")
print ("|  04  | Joker              | Rp.65.000 |")
print ("|  05  | Frozen II          | Rp.50.000 |")
print ("-----------------------------------------")
    

def hitung_diskon(total):
   if total >= 250000:
        return total * 0.35
   if total >= 100000:
        return total * 0.15
   return 0

def pesan_tiket():
    kode_pilihan = input("Masukkan kode film: ")
    if kode_pilihan in daftar_film:
        jumlah_tiket = int(input("Masukkan jumlah tiket: "))
        nama_pemesan = input("Masukkan nama Anda: ")
        judul, harga = daftar_film[kode_pilihan]
        total_harga = harga * jumlah_tiket
        diskon = hitung_diskon(total_harga)
        total_setelah_diskon = total_harga - diskon
        
        print(f"\n===== Struk Pemesanan =====")
        print(f"Nama        : {nama_pemesan}")
        print(f"Judul Film  : {judul}")
        print(f"Tiket       : {jumlah_tiket} x Rp{harga}")
        print(f"Diskon      : Rp{diskon}")
        print(f"Total Harga : Rp{total_setelah_diskon}")
        print(f"===========================")
    else:
        print("Kode film tidak ditemukan.")
        
pesan_tiket()
