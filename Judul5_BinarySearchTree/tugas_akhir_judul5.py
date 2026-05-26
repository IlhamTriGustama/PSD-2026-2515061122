class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)
        if nilai < root.nilai:
            root.left = self.insert_node(root.left, nilai)
        elif nilai > root.nilai:
            root.right = self.insert_node(root.right, nilai)
        return root

    def insert(self, nilai):
        self.root = self.insert_node(self.root, nilai)

    def search_node(self, root, nilai):
        if root is None:
            return False
        if root.nilai == nilai:
            return True
        if nilai < root.nilai:
            return self.search_node(root.left, nilai)
        return self.search_node(root.right, nilai)

    def search(self, nilai):
        return self.search_node(self.root, nilai)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.nilai, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.nilai, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.nilai, end=" ")


def main():
    bst = BST()
    pilih = 0

    while pilih != 6:
        print("\n=== PROGRAM PENDATAAN NILAI MAHASISWA ===")
        print("1. Tambah Nilai")
        print("2. Cari Nilai")
        print("3. Tampilkan Inorder")
        print("4. Tampilkan Preorder")
        print("5. Tampilkan Postorder")
        print("6. Keluar")

        try:
            pilih = int(input("Masukkan pilihan: "))

        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            try:
                nilai = int(input("Masukkan nilai mahasiswa: "))
                bst.insert(nilai)
                print("Nilai berhasil ditambahkan")

            except ValueError:
                print("Input harus berupa angka!")

        elif pilih == 2:
            try:
                nilai = int(input("Masukkan nilai yang dicari: "))

                if bst.search(nilai):
                    print("Nilai ditemukan")

                else:
                    print("Nilai tidak ditemukan")

            except ValueError:
                print("Input harus berupa angka!")

        elif pilih == 3:
            print("Data inorder : ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Data preorder : ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Data postorder : ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            print("Program selesai")

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
