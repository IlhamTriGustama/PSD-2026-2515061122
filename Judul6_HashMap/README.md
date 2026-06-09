JUDUL PROGRAM  : Program Manajemen Kontak Telepon Menggunakan Hash Map Separate Chaining

DESKRIPSI SINGKAT  :

A. PENJELASAN FUNGSI PROGRAM

Program Manajemen Kontak Telepon Menggunakan Hash Map Separate Chaining merupakan program yang digunakan untuk menyimpan dan mengelola data kontak telepon secara sederhana. Setiap kontak terdiri dari nomor telepon sebagai key dan nama kontak sebagai value. Program menyediakan beberapa fitur utama, yaitu menambahkan kontak baru, mencari kontak berdasarkan nomor telepon, menghapus kontak, serta menampilkan seluruh data kontak yang tersimpan di dalam hash table.

B. PENJELASAN ALGORITMA HASH MAP

Struktur data yang digunakan pada program ini adalah Hash Map dengan metode Separate Chaining untuk menangani collision. Setiap data kontak disimpan pada bucket yang ditentukan oleh fungsi hash, sedangkan data yang memiliki hasil hash yang sama akan disimpan dalam bentuk linked list pada bucket yang sama. Dengan menggunakan metode ini, proses penyimpanan, pencarian, dan penghapusan data dapat dilakukan dengan lebih efisien dibandingkan pencarian secara linear pada daftar data biasa.

SOURCE CODE  :

<img width="691" height="862" alt="Screenshot 2026-06-09 201919" src="https://github.com/user-attachments/assets/0f564c0d-7287-4f07-8a15-a182fcd717f4" />

<img width="770" height="789" alt="Screenshot 2026-06-09 201950" src="https://github.com/user-attachments/assets/b15afab3-2563-4529-af85-b38f6163abe9" />

<img width="825" height="770" alt="Screenshot 2026-06-09 202016" src="https://github.com/user-attachments/assets/a2f167e9-fefe-48ab-883a-508f46e09cf4" />

<img width="738" height="143" alt="Screenshot 2026-06-09 202037" src="https://github.com/user-attachments/assets/665478b2-ec59-4392-91d7-4623fb356acb" />

1. class Node:

     def __init__(self, key, value):
   
          self.key = key
   
          self.value = value
   
          self.next = None

Class Node digunakan untuk membuat node pada linked list. Setiap node menyimpan nomor telepon sebagai key, nama kontak sebagai value, dan pointer next             yang digunakan untuk menghubungkan node dengan node berikutnya.

2. def __init__(self, size=10):

        self.SIZE = size

        self.table = [None] * self.SIZE

Constructor digunakan untuk membuat hash table dengan ukuran tertentu. Pada program ini ukuran default hash table adalah 10 bucket yang masing-masing              diinisialisasi dengan nilai None.

3. def hash_function(self, key):

        return (key % self.SIZE + self.SIZE) % self.SIZE

Fungsi hash_function() digunakan untuk menentukan indeks penyimpanan data pada hash table berdasarkan nomor telepon yang dimasukkan. Hasil perhitungan             hash digunakan sebagai lokasi penyimpanan data.

4. def insert(self, key, value):

        index = self.hash_function(key)

Fungsi insert() digunakan untuk menambahkan data kontak ke dalam hash table. Jika nomor telepon sudah ada maka data akan diperbarui, sedangkan jika                terjadi collision data akan disimpan pada linked list menggunakan metode Separate Chaining.

5. def search(self, key):

        index = self.hash_function(key)

Fungsi search() digunakan untuk mencari data kontak berdasarkan nomor telepon. Program akan menelusuri linked list pada bucket yang sesuai hingga data             ditemukan atau tidak ditemukan.

6. def remove_key(self, key):

        index = self.hash_function(key)

Fungsi search() digunakan untuk mencari data kontak berdasarkan nomor telepon. Program akan menelusuri linked list pada bucket yang sesuai hingga data             ditemukan atau tidak ditemukan.

7. def display(self):

        print("\nDaftar Kontak:")

Fungsi search() digunakan untuk mencari data kontak berdasarkan nomor telepon. Program akan menelusuri linked list pada bucket yang sesuai hingga data             ditemukan atau tidak ditemukan.

<img width="668" height="664" alt="Screenshot 2026-06-09 212530" src="https://github.com/user-attachments/assets/51d40fef-102d-424e-8749-67a777223c21" />

<img width="627" height="651" alt="Screenshot 2026-06-09 212542" src="https://github.com/user-attachments/assets/81a65e93-164b-4ec9-9102-43875d084d7d" />

LINK YOUTUBE     : 



   






