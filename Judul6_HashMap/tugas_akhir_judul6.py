class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nDaftar Kontak:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    while True:
        print("\n=== MENU KONTAK TELEPON ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nomor = int(input("Masukkan nomor telepon: "))
            nama = input("Masukkan nama kontak: ")
            hashmap.insert(nomor, nama)
            print("Kontak berhasil ditambahkan.")
        elif pilihan == "2":
            nomor = int(input("Masukkan nomor telepon yang dicari: "))
            hasil = hashmap.search(nomor)
            if hasil is not None:
                print(f"Kontak ditemukan: {hasil.value}")
            else:
                print("Kontak tidak ditemukan.")
        elif pilihan == "3":
            nomor = int(input("Masukkan nomor telepon yang akan dihapus: "))
            if hashmap.remove_key(nomor):
                print("Kontak berhasil dihapus.")
            else:
                print("Kontak tidak ditemukan.")
        elif pilihan == "4":
            hashmap.display()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
