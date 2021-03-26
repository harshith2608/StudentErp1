from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/register')
def register():
    return render_template('Register.html')


@app.route('/home')
def home():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run()
