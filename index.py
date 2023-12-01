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
    b =  request.form.get('info')
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        print(b)
        return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)