# Athlete Training Management System

## Project Overview
A Flask-based web application for managing athletes, their training schedules, meals, supplements, and competitions.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Core Features](#core-features)
- [License](#license)

## Features
- 🏃‍♂️ **Athlete Management**
  - Profile tracking
  - Statistics monitoring
  - Performance metrics
- 📅 **Training Schedule** 
  - Create/edit schedules
  - Assign trainers
- 🍽️ **Meal Planning**
  - Meal tracking
  - Nutritional calculations
  - Ingredient management
- 💊 **Supplement Management**
  - Dosage tracking
  - Intake scheduling
- 🏆 **Competition Tracking**
  - Event management
  - Results recording
- 👥 **Staff Management**
  - Trainer assignments
  - Doctor consultations

## Tech Stack
- **Backend**: Python 3.12, Flask framework
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Architecture**: MVC pattern

## Project Structure
```
app/
├── controller/     # Request handlers
├── dao/           # Database operations
├── domain/        # Data models
├── root/          # Route definitions
├── service/       # Business logic
└── config.py      # Configuration
```

## Installation
1. **Clone repository**
```bash
git clone https://github.com/nezeracuk/database-labs-LPNU.git
```

2. **Create virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r app/requirements.txt
```

4. **Configure database**
```python
# filepath: app/config.py
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/dbname"
```

5. **Initialize database**
```bash
python app.py
```

## API Documentation
### Endpoints
- `/athlete` - Athlete CRUD operations
- `/competition` - Competition management
- `/meal` - Meal and nutrition tracking
- `/schedule` - Training schedule management
- `/trainer_doctor` - Staff management
- `/supplement` - Supplement tracking

## Database Schema
### Core Tables
- `athlete` - Athlete information
- `competition` - Competition details
- `meal` - Meal records
- `schedule` - Training schedules
- `trainer_doctor` - Staff records
- `supplement` - Supplement information
- `athlete_trainer` - Relationship mapping
- `athlete_statistics` - Performance metrics

## Core Features
### Data Management
- Complete CRUD operations
- Relationship handling
- Data validation

### Business Logic
- Energy calculations
- Statistics tracking
- Automated table creation
- Data validation triggers
