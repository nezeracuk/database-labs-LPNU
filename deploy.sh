#!/bin/bash

# Скрипт для швидкого деплою на AWS EC2
# Використання: ./deploy.sh

echo "====================================="
echo "Starting deployment..."
echo "====================================="

# Зупинити при помилці
set -e

# Переход в директорію проекту
cd ~/athlete-training-management-system || cd /home/admin/athlete-training-management-system

# Отримання останніх змін з Git
echo "Pulling latest changes from Git..."
git pull origin main

# Активація віртуального середовища
echo "Activating virtual environment..."
source venv/bin/activate

# Оновлення залежностей
echo "Installing dependencies..."
pip install -r app/requirements.txt

# Перезапуск сервісу (якщо налаштовано systemd)
echo "Restarting service..."
if systemctl is-active --quiet athlete-api; then
    sudo systemctl restart athlete-api
    echo "Service restarted successfully"
else
    echo "Service not found. Starting application manually..."
    # Запуск через gunicorn (для тестування)
    # gunicorn --bind 0.0.0.0:5000 wsgi:app &
fi

echo "====================================="
echo "Deployment completed at $(date)"
echo "====================================="

