class NhanVien:
    def __init__(self, name, age, salary):
        self.hoten = name
        self.tuoi = age
        self.luong = salary

    def __str__(self):
        message = 'Họ tên: ' + self.hoten + ' | Tuổi: ' + str(self.tuoi) + ' | Lương: ' + str(self.luong)
        return message

    def __gt__(self, other):
        return self.tuoi > other.tuoi

    def __ge__(self, other):
        return self.tuoi >= other.tuoi

    def __lt__(self, other):
        return self.tuoi < other.tuoi

    def __le__(self, other):
        return self.tuoi <= other.tuoi

    def __eq__(self, other):
        return self.tuoi == other.tuoi
