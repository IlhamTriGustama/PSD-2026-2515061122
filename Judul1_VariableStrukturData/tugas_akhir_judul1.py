# Program: TaskFlow - Sistem Manajemen Tugas Harian Sederhana Berbasis List

def tampilkan_menu():
    print("\n====== TaskFlow ======")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def tambah_tugas(tugas):
    nama_tugas = input("Tugas apa yang mau kamu buat? ")
    tugas.append({"nama": nama_tugas, "status": "Belum diselesaikan"})
    print("Tugas berhasil ditambahkan!")


def lihat_tugas(tugas):
    if len(tugas) == 0:
        print("Wah belum ada tugas nih hari ini, nyantai dulu kali yak^^")
    else:
        print("\nDaftar Tugas:")
        for i, t in enumerate(tugas):
            print(f"{i+1}. {t['nama']} - {t['status']}")


def tandai_selesai(tugas):
    if len(tugas) == 0:
        print("Kamu belum punya tugas untuk hari ini, jadi gaperlu ada yang harus diselesaiin^^")
    else:
        nomor = int(input("Tugas nomor berapa yang udah kamu selesaiin? ")) - 1
        if 0 <= nomor < len(tugas):
            tugas[nomor]["status"] = "Selesai"
            print("Yey satu tugas udah berhasil kamu selesaiin!")
        else:
            print("Nomor tidak valid.")


def hapus_tugas(tugas):
    if len(tugas) == 0:
        print("Kamu belum punya tugas untuk dihapus, jadi tenang saja^^")
    else:
        nomor = int(input("Tugas nomor berapa yang mau kamu hapus? ")) - 1
        if 0 <= nomor < len(tugas):
            tugas.pop(nomor)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tidak valid.")


def main():
    tugas = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_tugas(tugas)
        elif pilihan == "2":
            lihat_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        elif pilihan == "5":
            print("Makasih udah gunain TaskFlow!! Jangan lupa buat catat dan cek ulang tugas kamu setiap hari biar jadwal kamu ga berantakan^^!")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
