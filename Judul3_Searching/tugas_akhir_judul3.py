def sequential_search(games, n, target):
    i = 0
    while i < n:
        if games[i].lower() == target.lower():
            return i
        i += 1
    return -1


def main():
    games = [ "Elden Ring", "Genshin Impact", "Valorant", "Dragons Dogma", "Skyrim", "Dark souls", "The Witcher", "Silent Hill", 
                "Resident Evil", "Final Fantasy", "Persona", "Assassin's Creed", "Stardew Valley", "Hollow Knight", "Peak"
    ]
    n = len(games)
    print("=== Program Pencarian Game Favorit ===")
    target = input("\nMasukkan nama game yang pengen kamu cari: ")
    hasil = sequential_search(games, n, target)
    if hasil != -1:
        print(f"\nGame '{target}' adalah game terfavorit dan paling banyak dimainkan pada urutan nomor-{hasil + 1} untuk saat ini")
    else:
        print(f"\nGame '{target}' tidak ditemukan")

if __name__ == "__main__":
    main()
