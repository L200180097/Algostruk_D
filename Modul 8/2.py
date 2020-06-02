##Nomer 2
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
        
nilai = Stack() #membuat objek baru dari class Stack dengan nama nilai
for i in range (16): # melakukan perulangan dengan range 0 - 16
    if i % 3 == 0: #jika i mod 3 hasilnya 0 maka
        nilai.push(i) # tambahkan nilai i pada object nilai
        print (nilai.items)


