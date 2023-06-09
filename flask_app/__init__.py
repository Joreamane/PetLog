from flask import Flask
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask_app\static\petImages'
ALLOWED_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'fallon'