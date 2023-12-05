a = {
    'makan' : 'fuma',
    'tidur' : 'nolodo',
    'saya' : 'inodi',
    'aku' : 'inodi',
    'engkau' : 'ihintu',
    'dia' : 'anoa',
    'kami' : 'insaidi',
    'anda' : 'intaidi',
    'tuan' : 'intaidi',
    'mereka' : 'andoa',
    'ini' : 'aini',
    'itu' : 'aitu',
    'apa' : 'ohao',
    'mengapa' : 'neafa',
    'banyak' : 'noBari',
    'sedikit' : 'sendai',
    'sebahagian' : 'sega',
    'sebagian' : 'sega',
    'setengah' : 'selabunta',
    'besar' : 'nobala',
    'kecil' : 'norobu',
    'panjang' : 'newanta',
    'pendek' : 'noŋkubu'
}

class kamus:
    def __init__(self,kata):
        self.kata = kata
    
    def CekMu(self) -> str:
        for i in a:
            if self.kata == i:
                return a[i]
    def Cekin(self) -> str:
        for i in a:
            # print(f'i {i}')
            # print(f'a {a[i]}')
            # print(f'c {self.kata}')
            if self.kata == a[i]:
                print(i)

class terjemahan:
    def __init__(self,muna,indo,pasw):
        self.muna =  muna
        self.indo =  indo
        self.pasw =  pasw

    def tambah(self):
        x = self.muna
        y = self.indo
        __pw = self.pasw
        if __pw == '123':
            a[y] = x
            print(a)

# terjemahan('go','pergi','123').tambah()
# a = kamus('makan').CekMu()
# print(a)
# kamus('nolodo').Cekin()