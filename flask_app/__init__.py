from flask import Flask

UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER']
app.secret_key = 'fallon'