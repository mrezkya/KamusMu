from flask import Flask, render_template, request
from oop import *

#init app
app = Flask('__name__')

aa = 'Bahasa Muna^'
bb = 'Bahasa Indonesia^'

@app.route('/', methods = ['POST', 'GET'])
def index():
    a = request.form.get('indo')
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # print(a)
        return render_template('index.html')

@app.route('/test', methods = ['POST', 'GET'])
def test():
    return render_template('test.html')
    
@app.route('/process', methods = ['POST','GET'])
def process():
    if request.method == 'POST':
        b =  request.form.get('muna')
        c = kamus(b).CekMu()

        # data dari modal
        AddMuna =  request.form.get('abc')
        AddIndo =  request.form.get('indoa')
        g =  request.form.get('pass')

        print(AddMuna)
        print(AddIndo)
        # tambahkan data ke dalam dictonary
        terjemahan(AddMuna,AddIndo,g).tambah()
        return render_template('index.html', d=c, b=b, aa=aa, a=b)
    elif request.method == 'GET':
        b =  request.form.get('muna')
        c = kamus(b).CekMu()
        # return render_template('index.html', d=c)
        return render_template('index.html', d=c, b=b)

if __name__ == '__main__':
    app.run(debug=True)