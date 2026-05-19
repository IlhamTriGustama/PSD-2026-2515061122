class StackAnime:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX - 1

    def push(self, anime):
        if self.is_full():
            print("Riwayat anime penuh")
            return

        self.top += 1
        self.stack[self.top] = anime
        print(f'Anime "{anime}" berhasil ditambahkan ke riwayat')

    def pop(self):
        if self.is_empty():
            print("Riwayat anime kosong")
            return

        anime_hapus = self.stack[self.top]
        self.top -= 1
        print(f'Anime "{anime_hapus}" berhasil dihapus dari riwayat')

    def peek(self):
        if self.is_empty():
            print("Riwayat anime kosong")
            return

        print(f'Anime yang terakhir kamu tonton: {self.stack[self.top]}')

    def display(self):
        if self.is_empty():
            print("Riwayat anime kosong")
            return

        print("\n=== Riwayat Nonton ===")
        for i in range(self.top, -1, -1):
            print(f"- {self.stack[i]}")


def main():
    riwayat = StackAnime()
    pilih = 0

    while pilih != 5:
        print("\n===== PROGRAM RIWAYAT ANIME =====")
        print("1. Tambah Anime")
        print("2. Hapus Anime Terakhir")
        print("3. Lihat Anime Terakhir")
        print("4. Tampilkan Semua Riwayat")
        print("5. Keluar")

        try:
            pilih = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Input harus berupa angka")
            continue

        if pilih == 1:
            anime = input("Masukkan judul anime: ")
            riwayat.push(anime)

        elif pilih == 2:
            riwayat.pop()

        elif pilih == 3:
            riwayat.peek()

        elif pilih == 4:
            riwayat.display()

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak tersedia")


if __name__ == "__main__":
    main()
