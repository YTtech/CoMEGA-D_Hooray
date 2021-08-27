from flask import Flask, render_template
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)