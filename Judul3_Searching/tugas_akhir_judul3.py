def sequential_search(games, n, target):
    i = 0

    while i < n:
        if games[i].lower() == target.lower():
            return i
        i += 1

    return -1


def main():
    games = [
        "Genshin Impact",
        "Valorant",
        "Minecraft",
        "Mobile Legends",
        "PUBG"
    ]

    n = len(games)

    print("=== Program Pencarian Game Favorit ===")

    target = input("Masukkan nama game yang ingin dicari: ")

    hasil = sequential_search(games, n, target)

    if hasil != -1:
        print(f"\nGame '{target}' ditemukan pada urutan ke-{hasil + 1}")
    else:
        print(f"\nGame '{target}' tidak ditemukan")


if __name__ == "__main__":
    main()
