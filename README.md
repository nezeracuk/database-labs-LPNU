# 🏃‍♂️ Athlete Training Management System

## 📖 Project Overview
A comprehensive Flask-based REST API for managing athletes, their training schedules, meals, supplements, and competitions. Deployed on AWS with MySQL database and full API documentation via Swagger UI.

## 🚀 Quick Links
- **📚 API Documentation (Swagger)**: `http://your-server:5000/api/docs`
- **🏠 Home Page**: `http://your-server:5000/`
- **💚 Health Check**: `http://your-server:5000/health`

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)

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

## 🛠 Tech Stack
- **Backend**: Python 3.12+, Flask 3.0.3
- **Database**: MySQL 8.3.0
- **ORM**: SQLAlchemy 2.0.36
- **API Documentation**: Flasgger (Swagger UI)
- **Production Server**: Gunicorn
- **Cloud**: AWS EC2 + RDS
- **CI/CD**: GitHub Actions
- **Architecture**: MVC pattern with service layer

## 📁 Project Structure
```
athlete-training-management-system/
├── app/
│   ├── __init__.py           # Flask app + Swagger configuration
│   ├── config.py             # Database configuration
│   ├── database.py           # SQLAlchemy setup
│   ├── requirements.txt      # Python dependencies
│   ├── controller/           # Business logic controllers
│   ├── dao/                  # Data Access Objects
│   ├── domain/               # Database models (SQLAlchemy)
│   ├── root/                 # Flask Blueprints (API routes)
│   └── service/              # Service layer
├── db_scripts/
│   ├── triggers.sql          # MySQL triggers
│   └── cursor.sql            # MySQL stored procedures
├── .github/workflows/
│   └── deploy.yml            # GitHub Actions CI/CD
├── app.py                    # Development entry point
├── wsgi.py                   # Production entry point (Gunicorn)
├── create_db.py              # Database initialization script
├── deploy.sh                 # Deployment script
├── data.sql                  # Sample data
├── .gitignore                # Git ignore rules
├── AWS_DEPLOYMENT.md         # AWS deployment guide
├── QUICKSTART.md             # Quick start guide
├── LAB_REPORT.md             # Lab work report
└── README.md                 # This file
```

## ⚡ Quick Start

### Local Development

1. **Clone repository**
```bash
git clone https://github.com/YOUR_USERNAME/athlete-training-management-system.git
cd athlete-training-management-system
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# або
.\venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install -r app/requirements.txt
```

4. **Configure database**
Edit `app/config.py`:
```python
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host/skibytskyi2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

5. **Create database tables**
```bash
python3 create_db.py
```

6. **Run application**
```bash
# Development
python3 app.py

# Production
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

7. **Access the application**
- Home: http://localhost:5000/
- Swagger UI: http://localhost:5000/api/docs
- Athletes: http://localhost:5000/athlete

### AWS Deployment

See detailed instructions in:
- **📄 [AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md)** - Full deployment guide
- **📄 [QUICKSTART.md](QUICKSTART.md)** - Quick reference
- **📄 [ЩО_РОБИТИ_ЗАРАЗ.md](ЩО_РОБИТИ_ЗАРАЗ.md)** - Ukrainian step-by-step guide

## 📚 API Documentation

### Interactive Documentation
Visit **Swagger UI** at `http://your-server:5000/api/docs` for:
- 📖 Full API documentation
- 🧪 Interactive endpoint testing
- 📝 Request/response schemas
- ✅ Try it out directly in the browser

### Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with endpoint list |
| GET | `/api/docs` | Swagger UI documentation |
| GET | `/health` | Health check |
| GET/POST | `/athlete` | List/create athletes |
| GET/PUT/DELETE | `/athlete/{id}` | Get/update/delete athlete |
| GET/POST | `/statistics` | Athlete statistics |
| GET/POST | `/competition` | Competition management |
| GET/POST | `/trainer_doctor` | Trainer management |
| GET/POST | `/schedule` | Schedule management |
| GET/POST | `/meal` | Meal tracking |
| GET/POST | `/ingredient` | Ingredient management |
| GET/POST | `/supplement` | Supplement tracking |

### Example Requests

```bash
# Get all athletes
curl http://localhost:5000/athlete

# Create an athlete
curl -X POST http://localhost:5000/athlete \
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "Ivan",
    "lastname": "Petrov",
    "height": 180.5,
    "weight": 75.0
  }'

# Get athlete statistics
curl http://localhost:5000/statistics
```

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

## 🚢 Deployment

### Manual Deployment
```bash
./deploy.sh
```

### Automatic Deployment (CI/CD)
Push to main branch triggers automatic deployment via GitHub Actions:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

**Setup GitHub Secrets:**
- `EC2_HOST` - Your EC2 IP address
- `EC2_USERNAME` - SSH username (e.g., `admin`)
- `EC2_SSH_KEY` - Your private SSH key

## 🧪 Testing

```bash
# Health check
curl http://localhost:5000/health

# Get all endpoints
curl http://localhost:5000/

# Test athlete endpoint
curl http://localhost:5000/athlete
```

## 🐛 Troubleshooting

### Table doesn't exist error
```bash
python3 create_db.py
```

### Port already in use
```bash
sudo lsof -i :5000
sudo kill -9 <PID>
```

### Database connection error
Check `app/config.py` for correct credentials.

## 📝 Documentation

- **[AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md)** - Complete AWS deployment guide
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide
- **[LAB_REPORT.md](LAB_REPORT.md)** - Lab work report
- **[ЩО_РОБИТИ_ЗАРАЗ.md](ЩО_РОБИТИ_ЗАРАЗ.md)** - Step-by-step guide (Ukrainian)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the Database course at Lviv Polytechnic National University.

## 👨‍💻 Author

Your Name - [GitHub Profile](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- Course: "Бази даних і знань" (Databases and Knowledge)
- Lviv Polytechnic National University
- AWS for cloud infrastructure
