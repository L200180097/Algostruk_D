class simpulbiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranPohon(akar, count=0):
    if akar is None:
        return count

    return ukuranPohon(akar.kiri, ukuranPohon(akar.kanan, count+1))

A = simpulbiner ( 'Ambarawa' )
B = simpulbiner ( 'Bantul' )
C = simpulbiner ( 'Cimahi' )
D = simpulbiner ( 'Denpasar' )
E = simpulbiner ( 'Enrekang' )
H = simpulbiner ( 'Halmahera Timur' )


A . kiri = B ; A . kanan = C
B . kiri = D ; B . kanan = E
D . kiri = H ;
