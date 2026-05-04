JUDUL PROGRAM  : Program Pengurutan Leaderboard Game Menggunakan Bubble Sort (Descending)

DESKRIPSI SINGKAT : 

A. PENJELASAN FUNGSI PROGRAM

Program yang dibuat merupakan sebuah simulasi sederhana dari sistem leaderboard pada game, yang berfungsi untuk mengurutkan data pemain berdasarkan skor yang diperoleh. Pengguna dapat memasukkan beberapa data berupa nama pemain dan skor, kemudian program akan menampilkan data tersebut sebelum dan sesudah dilakukan proses pengurutan. Fungsi utama dari program ini adalah untuk membantu menentukan urutan peringkat pemain dari skor tertinggi ke terendah. Dengan adanya proses sorting, data yang awalnya tidak terurut dapat disusun menjadi lebih terstruktur sehingga memudahkan dalam melihat pemain dengan performa terbaik. Program ini juga dapat digunakan sebagai contoh penerapan konsep pengolahan data dalam kehidupan nyata, khususnya dalam sistem peringkat pada permainan digital.

B. PENJELASAN ALGORITMA DAN SORTING YANG DIGUNAKAN

Algoritma sorting yang digunakan dalam program ini adalah Bubble Sort, yaitu metode pengurutan yang bekerja dengan cara membandingkan elemen yang bersebelahan, kemudian menukarnya jika urutannya tidak sesuai. Proses ini dilakukan secara berulang hingga seluruh data tersusun dengan benar. Dalam program ini, Bubble Sort dimodifikasi untuk mengurutkan data secara descending, sehingga skor tertinggi akan berada di posisi paling atas. Pada setiap iterasi, algoritma akan membandingkan skor dari dua pemain yang berdekatan. Jika skor pemain di posisi awal lebih kecil dibandingkan pemain berikutnya, maka kedua data tersebut akan ditukar posisinya. Proses ini terus dilakukan sampai tidak ada lagi pertukaran yang diperlukan, yang menandakan bahwa seluruh data sudah terurut.

SOURCE CODE :

<img width="887" height="671" alt="Screenshot 2026-05-04 195510" src="https://github.com/user-attachments/assets/dc021a98-674f-4783-87c5-1f7d5167de29" />

<img width="759" height="606" alt="Screenshot 2026-05-04 195725" src="https://github.com/user-attachments/assets/e40bbc93-f2e5-4106-a85b-84b4c02c3ece" />

1. def tukar(arr, i, j):

   Mendefinisikan sebuah fungsi bernama "tukar" dengan parameter "arr" yaitu list data, "i" yaitu indeks pertama, dan "j" indeks kedua. 

2. temp = arr[i]

   Menyimpan sementara nilai yang ada pada array di indeks "i" ke variabel "temp".

3. arr[i] = arr[j]

   Mengisi posisi i dengan nilai dari indeks j.

4. arr[j] = temp

   Mengisi posisi j dengan nilai yang tadinya telah disimpan di variabel temp. 

5. def bubble_sort(arr, n):

   Mendefinisikan sebuah fungsi bernama "bubble_sort" yang akan digunakan untuk melakukan sorting dengan parameter "arr" sebagai list, dan "n" yaitu banyak jumlah datanya. 

6. for i in range(n - 1):

   Perulangan luar atau loop utama, menentukan berapa kali proses pengurutan akan dilakukan.

7. for j in range(n - i - 1):

   Perulangan dalam atau loop pembanding, digunakan untuk membandingkan elemen satu dengan yang lain.

8. if arr[j]['skor'] < arr[j + 1]['skor']:

   Sebuah perkondision yang digunakan untuk membandingkan skor dua indeks yang bersebelahan, tanda "<" digunakan karena kita ingin melakukan pengurutan secara descending.

 9. tukar(arr, j, j + 1)

    Jika kondisi terpenuhi (skor atau nilai di kiri lebih kecil) maka akan ditukar dengan memanggil fungsi "tukar" untuk menukar posisi data.

12. except ValueError:
    
     print("Input tidak valid!")
    
     return

    Jika input bukan angka, program akan berhenti dengan "return".

14. data = []

    Membuat list kosong untuk menyimpan data.

15. nama = input(f"Nama player ke-{i+1}: ")

    Input nama player, "i+1" supaya dimulai dari 1, bukan 0.

16. data.append({'nama': nama, 'skor': skor})

    Menyimpan data ke dalam list.

17. for d in data:

    Loop untuk mengambil data.

18. print(f"{d['nama']} - {d['skor']}")

    Menampilkan nama dan skor.

19. bubble_sort(data, n)

    Memanggil fungsi sorting untuk mengurutkan data.

20. for i in range(n):

    Loop untuk menampilkan hasil.

21. print(f"{i+1}. {data[i]['nama']} - {data[i]['skor']}")

    Menampilkan ranking, "i+1" untuk menampilkan nomor urut, kemudian nama dan skor













   
