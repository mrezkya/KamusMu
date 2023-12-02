from flask import Flask, render_template, request

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
    
@app.route('/process', methods = ['POST'])
def process():
    b =  request.form.get('muna')
    c =  request.form.get('indo')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)