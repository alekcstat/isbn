import os
from flask import Flask
from models.user import db
from controllers.user_controller import *

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DB_USER='isbn' 
DB_PASSWORD='123'
# DB_HOST=34.48.29.147 db
DB_HOST='34.70.158.47'
DB_NAME='ntc-companies-db1'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME 
db.init_app(app)

app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))