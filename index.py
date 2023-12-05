from flask import Flask, render_template, request
from oop import *

#init app
app = Flask('__name__')

@app.route('/', methods = ['POST', 'GET'])
def index():
    a = request.form.get('indo')
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(a)
        return render_template('index.html')

@app.route('/test', methods = ['POST', 'GET'])
def test():
    return render_template('test.html')
    
@app.route('/process', methods = ['POST','GET'])
def process():
    if request.method == 'POST':
        b =  request.form.get('muna')
        c = kamus(b).CekMu()
        return render_template('index.html', d=c)
    elif request.method == 'GET':
        b =  request.form.get('muna')
        c = kamus(b).CekMu()
        return render_template('index.html', d=c)

if __name__ == '__main__':
    app.run(debug=True)