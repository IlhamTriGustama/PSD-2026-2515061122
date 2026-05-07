JUDUL PROGRAM  : Pencarian Game Terfavorit Menggunakan Sequential Search

DESKRIPSI SINGKAT  : 

A. PENJELASAN FUNGSI PROGRAM

Program ini digunakan untuk mencari nama game berdasarkan input dari pengguna. Program akan memeriksa data game yang tersimpan di dalam list, kemudian menampilkan posisi game apabila ditemukan dan menampilkan pesan apabila game tidak ditemukan.

B. PENJELASAN ALGORITMA SEQUENTIAL SEARCH

Algoritma Sequential Search merupakan metode pencarian data yang dilakukan secara berurutan dari data pertama hingga data terakhir. Pada program ini, algoritma Sequential Search diterapkan menggunakan perulangan while untuk membandingkan setiap nama game dengan input pengguna sampai data ditemukan atau seluruh data selesai diperiksa.

SOURCE CODE  :

<img width="1067" height="576" alt="Screenshot 2026-05-07 224232" src="https://github.com/user-attachments/assets/862e9688-62d5-4fa7-9522-bd9e87a7e51b" />

1. def sequential_search(games, n, target):

   Mendefinisikan fungsi bernama sequential_search.

2. i = 0

   Variabel i digunakan sebagai penunjuk index atau posisi data yang sedang diperiksa. Nilai awal dibuat 0 karena index list di Python dimulai dari 0.

3. while i < n:

   Melakukan perulangan selama nilai i masih lebih kecil dari jumlah data (n).

4. if games[i].lower() == target.lower():

   Digunakan untuk membandingkan data game pada index ke-i dengan input pengguna. Fungsi .lower() digunakan agar huruf besar dan kecil dianggap sama sehingga pencarian menjadi lebih fleksibel.

5. return i

   Menambah nilai i sebanyak 1 agar program dapat memeriksa data berikutnya pada list.

6. i += 1

   Menambah nilai i sebanyak 1 agar program dapat memeriksa data berikutnya pada list.

7. return -1

   Jika seluruh data telah diperiksa tetapi game tidak ditemukan, maka fungsi akan mengembalikan nilai -1 sebagai tanda bahwa data tidak ada di dalam list.

8. n = len(games)

   Menghitung jumlah data game menggunakan fungsi len(), kemudian hasilnya disimpan ke dalam variabel n.

9. hasil = sequential_search(games, n, target)

    Memanggil fungsi sequential_search dengan mengirimkan data game, jumlah data, dan input pengguna. Hasil pencarian disimpan ke dalam variabel hasil.

10. if hasil != -1:

    Mengecek apakah data ditemukan. Jika nilai hasil tidak sama dengan -1, berarti game ditemukan.




