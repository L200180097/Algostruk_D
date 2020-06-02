class simpulbiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar, count=0):
    if akar is None:
        return 0
    else:
        return max(tinggiPohon(akar.kiri), tinggiPohon(akar.kanan))+1

A = simpulbiner ( 'Ambarawa' )
B = simpulbiner ( 'Bantul' )
C = simpulbiner ( 'Cimahi' )
D = simpulbiner ( 'Denpasar' )
E = simpulbiner ( 'Enrekang' )
H = simpulbiner ( 'Halmahera Timur' )


A . kiri = B ; A . kanan = C
B . kiri = D ; B . kanan = E
D . kiri = H ;
