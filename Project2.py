import random

def tentukan_nyawa(level):
    if level == "mudah":
        return 7
    elif level == "sedang":
        return 5
    elif level == "sulit":
        return 3
    pass

def main_angka():
    High_score = 0

    while True:
        print("\n" + "="*20)
        print(f"HIGH SCORE SAAT INI : {High_score}")
        print( "="*20)

        print("=== SELAMAT DATANG DI GAME TEBAK ANGKA ===")

        level = input("Silahkan Memilih level (mudah, sedang, sulit): ").lower()
        nyawa = tentukan_nyawa(level)
        angka_rahasia = random.randint(1, 50)
        skor_saat_ini = 100
        print(f"\nAku sudah memilih angka dari 1-50, kamu hanya punya {nyawa} nyawa, coba tebak!")

        while nyawa > 0:
            try:
                tebakan_angka = int(input(f"\n[{nyawa} nyawa tersisa] Masukkan tebakkanmu: "))
            except ValueError:
                print("Bos, Angka, bukan huruf!")
                continue
        
            selisih = abs(tebakan_angka - angka_rahasia)
            if tebakan_angka == angka_rahasia:
                print(f"\nHore!! Kamu menang! Angka rahasia adalah {angka_rahasia}. Yuk main lagi!")
                if skor_saat_ini > High_score:
                    High_score = skor_saat_ini
                    print(f"REKOR BARU! Skor tertinggi: {High_score}")
                else:
                    print(f"Skor kamu: {skor_saat_ini}. Rekor tertinggi: {High_score}.")
                break   
            elif selisih <= 3:
                print("Tebakanmu udah dekat, dikit lagi!")
            elif tebakan_angka < angka_rahasia:
                print("Masih terlalu kecil, tebak lagi!, semangat....")
            else:
                print("Masih terlalu besar, turun lagi!")

            skor_saat_ini -= 10
            nyawa -= 1
            if nyawa == 0:
                print(f"Game over!, Angka rahasianya adalah {angka_rahasia}. Yuk, coba lagi!")

        lagi = input("\nIngin main lagi? (y/n): ").lower()
        if lagi != "y":
            print("Baiklah, terimakasih telah bermain!")
            break


main_angka()
