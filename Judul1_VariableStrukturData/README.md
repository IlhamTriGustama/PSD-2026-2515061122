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


OUTPUT PROGRAM :

<img width="327" height="177" alt="Screenshot 2026-04-29 205131" src="https://github.com/user-attachments/assets/45a8b307-4e92-4722-91da-a5172a9a3031" />

Pengguna memilih menu 1 (Tambah Tugas), lalu memasukkan tugas

<img width="476" height="80" alt="Screenshot 2026-04-29 205426" src="https://github.com/user-attachments/assets/4ada5839-482f-4634-8875-c31f4587ac15" />

<img width="409" height="257" alt="Screenshot 2026-04-29 205645" src="https://github.com/user-attachments/assets/ec90c9ae-bd29-4712-89d3-d19aa3e915f0" />

Pengguna memilih menu 2 (Lihat Tugas)

<img width="480" height="75" alt="Screenshot 2026-04-29 205853" src="https://github.com/user-attachments/assets/6253959c-2a35-4953-a0c1-bf7f1719ec84" />

Pengguna menandai tugas pertama sebagai selesai

<img width="351" height="120" alt="Screenshot 2026-04-29 205951" src="https://github.com/user-attachments/assets/9a2ed97d-d812-4125-b75d-757dac25654f" />

Jika dilihat kembali

<img width="417" height="75" alt="Screenshot 2026-04-29 210122" src="https://github.com/user-attachments/assets/c5ad0f7b-8b32-49a2-afca-ecd048cc98b3" />

Pengguna menghapus tugas pertama

<img width="335" height="106" alt="Screenshot 2026-04-29 210229" src="https://github.com/user-attachments/assets/0efd834d-5126-4539-9aab-28f186cfb611" />

Jika dilihat kembali

<img width="1126" height="43" alt="Screenshot 2026-04-29 210352" src="https://github.com/user-attachments/assets/b9c6de68-0b4f-47bc-bda1-b2fbc738c9d8" />

Terakhir, pengguna keluar dari program





