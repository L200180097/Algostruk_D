##Nomer 1
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Tidka bisa diintip. Stack kosong"
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Tidka bisa dipop dari Stack kosong"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

def cetakHexa(b):
    f = Stack()
    if b == 0:
        f.push(0)
    while b !=0:
        sisa = b%16
        b = b//16
        f.push(sisa)
        hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    hasil = ""
    for i in range (len(f)):
        hasil += str(hexa[f.pop()])
    return hasil
