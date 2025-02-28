class Aritmatika:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tambah(self):
        return self.x + self.y

    def kurang(self):
        return self.x - self.y

    def kali(self):
        return self.x * self.y

    def bagi(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Tidak bisa membagi dengan nol"
