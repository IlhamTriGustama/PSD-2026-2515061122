JUDUL PROGRAM  : Program Riwayat Anime yang Ditonton Menggunakan Stack Array

DESKRIPSI SINGKAT  :

A. PENJELASAN FUNGSI PROGRAM

Ini merupakan sebuah program sederhana untuk menyimpan riwayat anime yang telah ditonton oleh pengguna menggunakan struktur data Stack Array. Program ini memungkinkan pengguna untuk menambahkan judul anime ke dalam riwayat, menghapus riwayat anime terakhir, melihat anime terakhir yang ditonton, serta menampilkan seluruh daftar riwayat anime. Konsep yang digunakan pada program ini adalah Last In First Out (LIFO), di mana data terakhir yang dimasukkan akan menjadi data pertama yang dikeluarkan. Oleh karena itu, anime yang terakhir ditambahkan ke dalam riwayat akan berada pada posisi paling atas dan akan dihapus terlebih dahulu ketika pengguna memilih menu hapus.

B. PENJELASAN ALGORITMA STACK ARRAY

Struktur data Stack diterapkan menggunakan array dengan variabel top sebagai penanda posisi data paling atas. Operasi push digunakan untuk menambahkan anime ke dalam stack, sedangkan operasi pop digunakan untuk menghapus anime terakhir dari riwayat. Selain itu, program juga menggunakan operasi peek untuk melihat anime terakhir yang ditonton tanpa menghapus data, serta display untuk menampilkan seluruh isi stack dari atas ke bawah. Dengan penerapan Stack Array ini, program dapat mengelola data riwayat anime secara terstruktur dan sesuai dengan konsep LIFO.

SOURCE CODE  :

<img width="713" height="695" alt="Screenshot 2026-05-19 212159" src="https://github.com/user-attachments/assets/64617eba-c90e-4fe5-a1f6-0adb4d22b4eb" />

<img width="713" height="655" alt="Screenshot 2026-05-19 212251" src="https://github.com/user-attachments/assets/10bf48d4-a767-4673-af30-332b26e1f804" />

<img width="598" height="333" alt="Screenshot 2026-05-19 212311" src="https://github.com/user-attachments/assets/c63cdeb4-8fc5-4406-ad6e-a121855613af" />


1. class StackAnime:

   Digunakan untuk membuat class bernama StackAnime yang berfungsi sebagai struktur utama program Stack Array.

2. def __init__(self, max_size=100):

   Merupakan constructor yang akan otomatis dijalankan saat object dibuat. Parameter max_size=100 digunakan untuk menentukan kapasitas maksimal stack sebanyak 100 data.

3. self.MAX = max_size

   Menyimpan kapasitas maksimal stack ke dalam variabel MAX.

4. self.stack = [None] * self.MAX

   Membuat array/list dengan ukuran sesuai kapasitas stack dan seluruh isi awalnya bernilai None.

5. self.top = -1

   Variabel top digunakan untuk menandai posisi data paling atas pada stack. Nilai -1 digunakan untuk menandakan bahwa stack masih kosong dan belum memiliki data. -1 karena index python di mulai dari 0

6. def is_empty()

   Fungsi berisi perintah yang digunakan untuk memeriksa apakah stack dalam keadaan kosong. Jika variabel top bernilai -1, maka method akan mengembalikan nilai True yang berarti belum ada data di dalam stack.

7. def is_full()

   Fungsi berisi perintah yang digunakan untuk memeriksa apakah stack sudah penuh. Jika posisi top sudah berada pada indeks terakhir array, maka stack tidak dapat menerima data baru lagi.

8. def push()

   Digunakan untuk menambahkan judul anime baru ke dalam stack.

9. if self.is_full():

    Program akan mengecek terlebih dahulu apakah stack sudah penuh menggunakan fungsi is_full().

10. return

    Digunakan untuk menghentikan proses fungsi agar program tidak tetap memasukkan data saat stack penuh.

11. self.top += 1

    Variabel top dinaikkan satu posisi untuk menunjukkan lokasi data baru pada stack.

12. self.stack[self.top] = anime

      Data atau Judul anime yang dimasukkan pengguna akan disimpan pada posisi paling atas stack.

13. def pop()

    Fungsi yang digunakan untuk menghapus anime terakhir dari stack sesuai konsep Last In First Out (LIFO).

14. if self.is_empty():

    Program akan memeriksa terlebih dahulu apakah stack kosong menggunakan fungsi is_empty().

15. anime_hapus = self.stack[self.top]

    Data yang berada pada posisi paling atas stack disimpan sementara ke variabel anime_hapus.

16. self.top -= 1

    Posisi top dikurang satu untuk menandakan bahwa data paling atas telah dihapus dari stack.

17. def peek()

    Fungsi yang digunakan untuk melihat data terakhir yang berada di posisi paling atas stack tanpa menghapus data tersebut.

18. print(f'Anime terakhir ditonton: {self.stack[self.top]}')

    Menampilkan Data atau anime yang berada pada posisi paling atas stack atau anime terakhir yang ditonton pengguna.

19. def display()

    Fungsi yang digunakan untuk menampilkan seluruh riwayat data atau anime yang tersimpan di dalam stack.

20. for i in range(self.top, -1, -1):

    Perulangan yang digunakan untuk menampilkan isi stack dari posisi paling atas hingga paling bawah. Nilai -1 pada langkah perulangan menandakan bahwa perulangan bergerak mundur.

21. print(f"- {self.stack[i]}")

    Menampilkan setiap data atau dalam program ini yaitu judul anime yang tersimpan di dalam stack sesuai urutan LIFO.

22. riwayat = StackAnime()

    Membuat object riwayat dari class StackAnime agar seluruh method atau fungsi stack dapat digunakan di dalam program.

23. pilih = 0

    Variabel pilih digunakan untuk menyimpan pilihan menu dari pengguna. Nilai 0 adalah nilai awal sementara yang bersifat netral sebelum user memilih menu agar variabel pilih bisa terdefinisi.


OUTPUT PROGRAM

<img width="512" height="563" alt="Screenshot 2026-05-19 224556" src="https://github.com/user-attachments/assets/33a14431-b99f-467b-9d93-c1d63000e450" />

<img width="545" height="465" alt="Screenshot 2026-05-19 224612" src="https://github.com/user-attachments/assets/bc46be0c-7af9-47f7-9146-456c3fec3481" />






















   
