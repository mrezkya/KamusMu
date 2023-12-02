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

# a = kamus('makan').CekMu()
# print(a)