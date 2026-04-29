JUDUL PROGRAM     : Sistem Manajemen Tugas Harian Berbasil List


DESKRIPSI SINGKAT : 

A. PENJELASAN FUNGSI PROGRAM

Program ini berfungsi untuk membantu pengguna dalam mengelola daftar tugas harian secara sederhana. Pengguna dapat menambahkan tugas baru, melihat daftar tugas,
menandai tugas yang sudah selesai, serta menghapus tugas. Dalam program ini, struktur data yang digunakan adalah list yang berisi kumpulan data tugas. Dengan memanfaatkan list, program dapat melakukan operasi penambahan, penghapusan, dan perubahan data secara dinamis sesuai kebutuhan pengguna.

B. PENJELASAN ALGORITMA DAN STRUKTUR DATA

Algoritma yang digunakan dalam program ini bersifat iteratif dengan memanfaatkan perulangan while untuk menjalankan program secara terus-menerus hingga pengguna memilih untuk keluar. Setiap pilihan menu akan diproses menggunakan percabangan if-elif, sehingga program dapat menentukan tindakan yang sesuai berdasarkan input pengguna. Struktur data utama yang digunakan adalah list, yang memungkinkan penyimpanan data secara berurutan dan fleksibel. Operasi yang diterapkan pada list meliputi penambahan data menggunakan append(), penghapusan data menggunakan pop(), serta akses dan pembaruan data melalui indeks. Selain itu, digunakan perulangan for untuk menampilkan seluruh isi list kepada pengguna. Dengan kombinasi algoritma tersebut, program mampu berjalan secara sistematis dalam mengelola data tugas.

SOURCE CODE : 

<img width="1024" height="881" alt="Screenshot 2026-04-29 201449" src="https://github.com/user-attachments/assets/8a1832c8-bded-42b2-bab0-70892819754c" />

<img width="965" height="918" alt="Screenshot 2026-04-29 201551" src="https://github.com/user-attachments/assets/8e0a1d55-f275-4b23-b06d-b266cf490194" />

1. def tampilkan_menu():
   Mendefinisikan fungsi untuk menampilkan menu utama.

2. def tambah_tugas(tugas):
   Mendefinisikan fungsi untuk menambahkan tugas ke dalam list.

3. nama_tugas = input("Masukkan nama tugas: ")
   Menerima input nama tugas dari pengguna.

4. tugas.append({"nama": nama_tugas, "status": "Belum"})
   Menambahkan data tugas ke dalam list dalam bentuk dictionary.

5. def lihat_tugas(tugas):
   Fungsi untuk menampilkan daftar tugas.

6. if len(tugas) == 0:
   Mengecek apakah list kosong.

7. for i, t in enumerate(tugas):
   Melakukan perulangan untuk setiap elemen dalam list.

8. print(f"{i+1}. {t['nama']} - {t['status']}")
   Menampilkan nomor, nama tugas, dan statusnya.

9. def tandai_selesai(tugas):
    Fungsi untuk mengubah status tugas menjadi selesai.

10. nomor = int(input("Masukkan nomor tugas: ")) - 1
    Menerima input nomor tugas dan dikurangi 1 karena indeks dimulai dari 0.

11. if 0 <= nomor < len(tugas):
    Validasi nomor untuk memastikan apakah nomor yang dimasukkan valid.

12. tugas[nomor]["status"] = "Selesai"
    Mengubah status tugas menjadi selesai.

13. def hapus_tugas(tugas):
    Fungsi untuk menghapus tugas dari list.

14. tugas.pop(nomor)
    Menghapus elemen berdasarkan indeks.

15. def main():
    Fungsi utama yang menjalankan program.

16. tugas = []
    Membuat list kosong untuk menyimpan tugas.

17. while True:
    Perulangan tak terbatas agar program terus berjalan.

18. tampilkan_menu()
    Memanggil fungsi untuk menampilkan menu.

19. pilihan = input("Pilih menu (1-5): ")
    Menerima input pilihan dari pengguna.

20. if pilihan == "1":
            tambah_tugas(tugas)
    Menjalankan fungsi tambah tugas.

21. elif pilihan == "5":
            print("Terima kasih telah menggunakan TaskFlow!")
            break
    Menghentikan program.

22. if __name__ == "__main__":
    main()
    Menjalankan fungsi main() ketika program dieksekusi.












