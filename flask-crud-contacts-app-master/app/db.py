from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = "alumnopython"
app.config['MYSQL_PASSWORD'] = "programacionpython"
app.config['MYSQL_HOST'] = "db4free.net"
app.config['MYSQL_DB'] = "practicasql"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
