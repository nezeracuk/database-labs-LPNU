import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
try:
    from flasgger import Swagger
    HAS_SWAGGER = True
except ImportError:
    HAS_SWAGGER = False
    print("Warning: flasgger not installed. Swagger UI will not be available.")
from app.config import Config
from app.root import register_routes
import os
import sys
from app.database import db

print(sys.path)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Налаштування Swagger UI (якщо доступний)
    if HAS_SWAGGER:
        swagger_config = {
            "headers": [],
            "specs": [
                {
                    "endpoint": 'apispec',
                    "route": '/apispec.json',
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True,
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/api/docs"
        }
        
        swagger_template = {
            "info": {
                "title": "Athlete Training Management System API",
                "description": "REST API для системи управління тренуванням спортсменів",
                "version": "1.0.0",
                "contact": {
                    "name": "API Support",
                    "url": "https://github.com/yourusername/athlete-training-management-system",
                }
            },
            "host": "",  # Буде автоматично визначено
            "basePath": "/",
            "schemes": ["http", "https"],
        }
        
        Swagger(app, config=swagger_config, template=swagger_template)
    
    db.init_app(app)
    register_routes(app)
    return app



def create_database():
    # Використовуємо змінні середовища
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'your-password'),
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME', 'skibytskyi2')}")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'your-password'),
            database=os.getenv('DB_NAME', 'skibytskyi2')
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        print(f"SQL statement: {statement}")
                        connection.rollback()
        cursor.close()
        connection.close()

def execute_sql_scripts(file_names):
    """
    Виконує список SQL-скриптів, переданих у file_names.
    """
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'your-password'),
        database=os.getenv('DB_NAME', 'skibytskyi2')
    )
    cursor = connection.cursor()

    for file_name in file_names:
        file_path = os.path.abspath(file_name)
        if os.path.exists(file_path):
            print(f"Виконання SQL-скрипту: {file_name}")
            with open(file_path, 'r') as sql_file:
                sql_text = sql_file.read()
                sql_statements = sql_text.split(';')
                for statement in sql_statements:
                    statement = statement.strip()
                    if statement:
                        try:
                            cursor.execute(statement)
                            connection.commit()
                        except mysql.connector.Error as error:
                            print(f"Помилка виконання SQL-інструкції: {error}")
                            print(f"SQL-інструкція: {statement}")
                            connection.rollback()

    cursor.close()
    connection.close()

def execute_triggers():
    sql_file_path = os.path.abspath('../db_scripts/triggers.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'your-password'),
            database=os.getenv('DB_NAME', 'skibytskyi2')
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        print(f"SQL statement: {statement}")
                        connection.rollback()
        cursor.close()
        connection.close()

