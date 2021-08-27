from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main')
def game():
    return render_template('main.html')

@app.route('/point')
def point():
    return render_template('point.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.debug = True
    app.run()