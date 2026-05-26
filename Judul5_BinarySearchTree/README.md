JUDUL PROGRAM  : PROGRAM PENDATAAN NILAI MAHASISWA SEDERHANA MENGGUNAKAN BINARY SEARCH TREE

DESKRIPSI SINGKAT  :

A. PENJELASAN FUNGSI PROGRAM

Program yang dibuat merupakan program pendataan nilai mahasiswa sederhana menggunakan struktur data Binary Search Tree (BST). Program ini digunakan untuk menyimpan data nilai mahasiswa, mencari nilai tertentu, serta menampilkan data menggunakan metode traversal inorder, preorder, dan postorder. Data nilai yang dimasukkan akan disusun secara otomatis sesuai aturan BST, yaitu nilai yang lebih kecil ditempatkan pada subtree kiri dan nilai yang lebih besar ditempatkan pada subtree kanan.

B. PENJELASAN ALGORITMA BINARY SEARCH TREE

Algoritma struktur data yang diterapkan pada program ini adalah Binary Search Tree (BST). BST merupakan struktur data berbentuk tree yang memiliki node root, node kiri, dan node kanan. Program ini juga menerapkan konsep rekursi pada proses insert, search, dan traversal data. Traversal inorder digunakan untuk menampilkan data secara terurut, sedangkan preorder dan postorder digunakan untuk menampilkan data berdasarkan urutan penelusuran node tertentu.

SOURCE CODE  :

<img width="850" height="833" alt="Screenshot 2026-05-26 220633" src="https://github.com/user-attachments/assets/29f1aaf6-7f29-4883-9e90-7680c6b0756e" />

<img width="862" height="765" alt="Screenshot 2026-05-26 220658" src="https://github.com/user-attachments/assets/573af525-df0b-4997-b1b6-90c6ba51fa4f" />

<img width="868" height="809" alt="Screenshot 2026-05-26 220726" src="https://github.com/user-attachments/assets/a11bc52b-2619-4af8-9900-4455b38e2d32" />

<img width="855" height="485" alt="Screenshot 2026-05-26 220746" src="https://github.com/user-attachments/assets/87c230b1-2121-4531-9a9f-bd15c892cbad" />

1. class Node:
   
   Membuat class bernama "Node"

3. def __init__(self, nilai):
   
   Baris ini merupakan constructor pada class "Node". Memiliki parameter "self" yang merepresentasikan sebuah objek yang dibuat dari class, dan parameter "nilai" yang merepresentasikan nilai yang akan ingin dimasukkan ke dalam node.

5. self.nilai = nilai
   
   Untuk menyimpan data yang ada variabel "nilai" ke dalam node atau objek.

7. self.left = None
   
   Untuk membuat cabang yang akan menjadi subtree sebelah kiri. Nilai awalnya "None" karena pada kondisi awal root belum memiliki anak.

9. self.right = None
    
   Untuk membuat cabang yang akan menjadi subtree sebelah kanan. Nilai awalnya "None" karena pada kondisi awal root belum memiliki anak.

11. class BST:
    
   Membuat class bernama "BST"

13. def insert_node(self, root, nilai):
    
        if root is None:
    
            return Node(nilai)
    
        if nilai < root.nilai:
    
            root.left = self.insert_node(root.left, nilai)
    
        elif nilai > root.nilai:
    
            root.right = self.insert_node(root.right, nilai)
    
        return root

    Fungsi insert_node() digunakan untuk menambahkan data nilai mahasiswa ke dalam Binary Search Tree menggunakan konsep rekursi. Fungsi ini akan memeriksa posisi node berdasarkan aturan BST, yaitu nilai yang lebih kecil dari root akan ditempatkan di subtree kiri dan nilai yang lebih besar akan ditempatkan di subtree kanan. Jika posisi node masih kosong (None), maka program akan membuat node baru menggunakan "class Node". Proses rekursi akan terus berjalan sampai posisi yang sesuai ditemukan.

14. def insert(self, nilai):
    
    self.root = self.insert_node(self.root, nilai)

    Fungsi insert() digunakan sebagai fungsi utama untuk memasukkan data ke BST. Fungsi ini memanggil fungsi insert_node() dan memulai proses insert dari root utama tree. Dengan adanya method ini, user cukup memanggil "insert()" tanpa perlu mengatur proses rekursi secara langsung.

15. def search_node(self, root, nilai):
    
    if root is None:
    
        return False

    if root.nilai == nilai:
    
        return True

    if nilai < root.nilai:
    
        return self.search_node(root.left, nilai)

    return self.search_node(root.right, nilai)

    Fugnsi search_node() digunakan untuk mencari data nilai pada BST menggunakan konsep rekursi. Program akan membandingkan nilai yang dicari dengan node saat ini. Jika nilai lebih kecil, pencarian dilakukan ke subtree kiri, sedangkan jika lebih besar maka pencarian dilakukan ke subtree kanan. Jika nilai ditemukan maka method mengembalikan True, sedangkan jika node kosong maka method mengembalikan False.

16. def search(self, nilai):
    
        return self.search_node(self.root, nilai)

    Fungsi search() digunakan sebagai fungsi utama untuk melakukan pencarian data pada BST. Fungsi ini memanggil fungsi search_node() dan memulai pencarian dari root utama tree sehingga user tidak perlu memanggil fungsi rekursif secara langsung.

17. def inorder(self, root):
    
        if root is not None:
    
            self.inorder(root.left)
    
            print(root.nilai, end=" ")
    
            self.inorder(root.right)

    Fungsi inorder() digunakan untuk menampilkan data BST menggunakan traversal inorder dengan urutan kiri lalu ke root dan kemudian ke kanan. Pada Binary Search Tree, traversal inorder akan menghasilkan data yang terurut dari nilai terkecil ke terbesar. Fungsi ini menggunakan rekursi untuk mengunjungi seluruh node pada tree.

18. def preorder(self, root):
    
        if root is not None:
    
            print(root.nilai, end=" ")
    
            self.preorder(root.left)
    
            self.preorder(root.right)

    Fungsi preorder() digunakan untuk menampilkan data BST menggunakan traversal preorder dengan urutan root lalu ke kiri dan kemudian ke kanan. Traversal ini digunakan untuk menampilkan struktur tree dimulai dari root terlebih dahulu sebelum menuju subtree kiri dan kanan.

19. def postorder(self, root):
    
        if root is not None:
    
            self.postorder(root.left)
    
            self.postorder(root.right)
    
            print(root.nilai, end=" ")

    Fungsi postorder() digunakan untuk menampilkan data BST menggunakan traversal postorder dengan urutan kiri lalu ke kanan dan kemudian ke root. Traversal ini akan mengunjungi subtree kiri dan kanan terlebih dahulu sebelum menampilkan node root.

OUTPUT PROGRAM   :

<img width="548" height="722" alt="Screenshot 2026-05-26 225157" src="https://github.com/user-attachments/assets/a1186853-43ff-4de0-8e50-25d3049f06d7" />

<img width="607" height="650" alt="Screenshot 2026-05-26 225218" src="https://github.com/user-attachments/assets/cee89ba6-85f1-426d-908d-cb8228aca09e" />

PENJELASAN OUTPUT PROGRAM   :

Pada output program di atas, pengguna memasukkan nilai mahasiswa yang bernilai 20, karena root dari Tree nya belum ada maka nilai 20 ini akan menjadi root dari Tree. Selanjutnya pengguna memasukkan nilai 10, karena 10 lebih kecil dari 20 maka nilai 10 akan turun ke subtree sebelah kiri. Kemudian pengguna memasukkan satu nilai lagi yaitu 40, karena 40 lebih besar dari root nya yaitu 20, maka 40 akan turun ke subtree sebelah kanan. Ketika pengguna memilih pilihan untuk menampilkan inorder, sistem akan menampilkan nilai yang ada pada tiap tiap node mulai dari kiri, ke root, dan ke kanan sehingga hasilnya akan menjadi terurut. Ketika pengguna memilih untuk menampilkan pilihan Tampilkan preorder, maka sistem akan menampilkan data pada Tree yang diakses mulai dari root, turun ke subree kiri, kemudian baru ke subtree sebelah kanan, dan ketika pengguna memilih pilihan tampilkan postorder, maka sistem akan menampilkan data pada Tree yang diakses mulai subtree kiri, ke subtree kanan, dan baru kemudian ke root.


    

    

   




