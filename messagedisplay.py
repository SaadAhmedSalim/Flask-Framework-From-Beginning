from flask import Flask, flash, redirect,render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template("messagedisplay.html")

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'INVALID UserName or Password. Please Try Again!'
        else:
            flash('Your are Successfully Logged IN!')
            flash('Log Out Before Login Again!')
            return redirect(url_for('index'))
    return render_template('loginMessage.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)