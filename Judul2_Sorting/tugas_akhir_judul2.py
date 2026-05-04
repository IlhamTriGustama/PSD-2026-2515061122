def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j]['skor'] < arr[j + 1]['skor']:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah player: "))
    except ValueError:
        print("Input tidak valid!")
        return

    data = []

    print("Masukkan data player (nama dan skor):")
    for i in range(n):
        nama = input(f"Nama player ke-{i+1}: ")
        
        while True:
            try:
                skor = int(input(f"Skor {nama}: "))
                break
            except ValueError:
                print("Input skor harus berupa angka!")

        data.append({'nama': nama, 'skor': skor})

    print("\nData sebelum diurutkan:")
    for d in data:
        print(f"{d['nama']} - {d['skor']}")

    bubble_sort(data, n)

    print("\nLeaderboard setelah diurutkan (Descending):")
    for i in range(n):
        print(f"{i+1}. {data[i]['nama']} - {data[i]['skor']}")


if __name__ == "__main__":
    main()
