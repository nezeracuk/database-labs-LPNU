from app import create_app, execute_sql_scripts, populate_data, create_tables, create_database

app = create_app()

with app.app_context():
    create_database()
    create_tables(app)
    print("Таблиці даних вже створені або існують.")
    populate_data()

    # Виконання додаткових SQL-скриптів
    execute_sql_scripts(['triggers.sql', 'functions.sql', 'stored_procedures.sql'])
    print("SQL-скрипти виконано.")


if __name__ == '__main__':
    app.run(debug=True)