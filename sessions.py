from flask import Flask, session, redirect,render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+ username + '<br/>'+ \
                "<b><a href='/logout'>Click Here to Log Out.</a></b>"
    return "YOU are not logged in <br><b><a href='/login'></b>" + \
                "Click here to Log In!</b></a>"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('sessions.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

