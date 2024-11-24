import os
from app import db


def execute_sql_file(file_path):
    """
    Виконує SQL-скрипт із вказаного файлу.
    """
    if not os.path.exists(file_path):
        print(f"SQL файл {file_path} не знайдено.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read()

    try:
        with db.engine.connect() as connection:
            for command in sql_commands.split(';'):
                if command.strip():
                    connection.execute(command)
        print(f"SQL файл {file_path} успішно виконано.")
    except Exception as e:
        print(f"Помилка виконання {file_path}: {e}")
