from models import Aritmatika

def main():
    master = "Mikhail Cychael"
    print(f"Welcome to UV Universe, {master}!\n")


    print("Aritmatika Sederhana")
    # Buat objek dari class Aritmatika
    aritmatika = Aritmatika(10, 5)
    print(f"10 + 5 = {aritmatika.tambah()}")
    print(f"10 - 5 = {aritmatika.kurang()}")
    print(f"10 * 5 = {aritmatika.kali()}")
    print(f"10 / 5 = {aritmatika.bagi()}")
    aritmatika = Aritmatika(10, 0)
    print(f"10 / 0 = {aritmatika.bagi()}")
    print("Terima kasih sudah menggunakan Aritmatika Sederhana")


if __name__ == "__main__":
    main()
