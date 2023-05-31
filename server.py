from flask_app import app
from flask_app.controllers import userroutes
from flask_app.controllers import petroutes

if __name__ == '__main__':
    app.run(debug=True)