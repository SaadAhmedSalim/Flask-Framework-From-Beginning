from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("setcookies.html")

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        response = make_response(render_template('readcookies.html'))
        response.set_cookie('USERID', user)
        return response

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('USERID')
    return '<h1> Welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)

