from flask import Flask
# from flask.ext.mail import Message, Mail
app = Flask(__name__)
# from flask_mail import Mail, Message
# mail.init_app(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'saadsalim283@gmail.com'
app.config['MAIL_PASSWORD'] = 'saadsalim278'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

@app.route("/")
def index():
    mesg = Message('Yo Baby', sender = 'saadsalim283@gmail.com', recipient =['saadsalim2782@gmail.com'])
    mesg.body = "Hello Flask! This message is sent from Flask Mail Server"
    mail.send(mesg)
    return "Message Sent"

if __name__ == '__main__':
    app.run(debug=True)