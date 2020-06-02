####No. 4A
##class Queue(object):
##    def __init__(self):
##        self.qlist = []
##
##    def isEmpty(self):
##        return len(self) == 0
##
##    def __len__(self):
##        return len(self.qlist)
##
##    def enqueue(self, data):
##        self.qlist.append(data)
##
##    def dequeue(self):
##        assert not self.isEmpty(), "Antrian sedang kosong"
##        return self.qlist.pop(0)
##
##    def getFrontMost(self):
##        return self.qlist[0]
##
##    def getRearMost(self):
##        return self.qlist[-1]
##    
##A = Queue()
##A.enqueue(18)
##A.enqueue(13)
##A.enqueue(45)
##A.enqueue(13)
##A.enqueue(11)
##
##print (A .qlist)
##print ("item yang paling depan :",A.getFrontMost())
##print ("item yang paling belakang :", A.getRearMost())











##Nomer 4B
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def getFrontMost(self):
        x = 0
        while self.qlist[x].priority != 0:
            x+=1
        return self.qlist[x].item

    def getRearMost(self):
        a = []
        for i in self.qlist:
            a.append(i.priority)
        print (self.qlist[a.index(max(a))].item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        
S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 4)
S.enqueue("Pepaya", 2)

print (S.qlist)
print ("item yang paling depan :",S.getFrontMost())
print ("item yang paling belakang :", S.getRearMost())

