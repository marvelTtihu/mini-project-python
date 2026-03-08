# Program Kasir Sederhana

def bersihkan_input(teks):
    return teks.replace(".", "").replace(",", "")

keranjang = []

total_harga = 0

while True:
    print("=== SELF CHECKOUT ===")
    nama_barang = (input("Masukkan Nama barang (atau ketik bayar): ")).strip()
    if nama_barang.lower() == "bayar":
       break
    if not nama_barang:
        print("Nama barang tidak boleh kosong.")
    if not nama_barang.replace(" ", "").isalpha():
        print("Nama barang harus berupa huruf. Tolong diulang kembali. ")
        continue
        
    while True:
        try:
            harga_barang = int(bersihkan_input(input("Masukkan Harga barang: ")))
            if harga_barang <= 0:
                print("Harga barang tidak valid, tolong masukkan ulang.")
                continue
            break
        except ValueError:
            print("Terjadi kesalahan. Silahkan masukkan ulang.")

    while True:
        try:
            jumlah_barang = int(input("Masukkan Jumlah barang: "))
            if jumlah_barang <= 0:
                print("\nJumlah barang tidak boleh negatif, tolong masukkan ulang.")
                continue
            if jumlah_barang >= 100:
                print("\nJumlah barang tidak boleh lebih dari 100, tolong masukkan ulang.")
                continue
            break
        except ValueError:
            print("Terjadi kesalahan. Tolong masukkan ulang.")

    subtotal = harga_barang * jumlah_barang
    diskon = subtotal * 0.1
    dpp = subtotal - diskon
    pajak = dpp * 0.11
    total_harga += dpp + pajak
    keranjang.append([nama_barang, harga_barang, jumlah_barang])

    tanya = input("\nIngin tambah barang lain? (y/n): ").lower().strip()
    if tanya == 'n' or tanya == 'bayar':
        break

print("\nStruk Pembayaran")
print("=" * 30)
for barang in keranjang:
    nama_barang = barang[0]
    harga_barang = barang[1]
    jumlah_barang = barang[2]

    subtotal = harga_barang * jumlah_barang
    print(f"{nama_barang:<15} | {jumlah_barang:>2} x Rp{harga_barang:>7,.0f} = Rp{subtotal:>10,.0f}")
print(f"Total Harga: Rp {total_harga:,.0f}")
print("=" * 30)
try:
    while True:
        pembayaran = int(bersihkan_input(input("Masukkan Pembayaran: ")))
        if pembayaran <= total_harga:
            print("Pembayaran tidak cukup. Silahkan masukkan ulang.")
        else:
            kembalian = pembayaran - total_harga
            print(f"Kembalian: Rp {kembalian:,.0f}")
            print("\nTerima kasih telah berbelanja di toko kami.")
            break
except ValueError:
    print("Terjadi kesalahan. Silahkan masukkan ulang.")
