from flask import Flask, abort, redirect,render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return render_template('index')

@app.route('/success')
def success():
    return 'Logged in Successfully!'

if __name__ == '__main__':
    app.run(debug=True)