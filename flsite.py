import sqlite3
import os
from flask import Flask, render_template, request


# Конфигурация WSGI приложения
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'sdg5cf2gh9sdf3se4f34'


app = Flask(__name__)
app.config.from_object(__name__) # загружаем конфигурацию WSGI приложения


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db'))) # переопределим путь к базе данных
