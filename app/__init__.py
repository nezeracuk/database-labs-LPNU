import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
import sys
from app.database import db

print(sys.path)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    register_routes(app)

    with app.app_context():
        create_database()
        create_tables(app)
        execute_triggers()  # Додай цей рядок
        print("Тригери створені.")
        populate_data()

    return app



def create_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='27102005',
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lab4")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='27102005',
            database='lab4'
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
        host='127.0.0.1',
        user='root',
        password='27102005',
        database='lab4'
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
            host='127.0.0.1',
            user='root',
            password='27102005',
            database='lab4'
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

