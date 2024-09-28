# Django Property Information Application

A Django-based application for managing and storing property information using Django admin. This project allows for efficient handling of property details, including images, locations, and amenities.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Prerequisites](#prerequisites)
5. [Project Structure](#project-structure)
6. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Database Configuration](#database-configuration)
   - [Running the Application](#running-the-application)
7. [Usage](#usage)
8. [Database Schema](#database-schema)
9. [CLI Data Migration](#cli-data-migration)
10. [Contributing](#contributing)
11. [License](#license)

## Project Overview

This Django application is designed to store and manage property information efficiently. It utilizes Django's powerful admin interface for CRUD operations and includes custom models to handle various aspects of property data, such as images, locations, and amenities.

## Features

- **Property Management**: Store and manage detailed property information.
- **Image Handling**: One-to-many relationship for property images.
- **Location Management**: Many-to-many relationship for property locations.
- **Amenity Tracking**: Many-to-many relationship for property amenities.
- **Django Admin Interface**: Customized admin panel for easy CRUD operations.
- **Data Migration**: CLI application to migrate data from a Scrapy project database.

## Technologies Used

- Backend: Python, Django
- Database: PostgreSQL
- ORM: Django ORM

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- PostgreSQL
- Git

**Note**: Please run the project from https://github.com/noman62/-web-scraper- according to the instructions in its README file, and place it in the same directory as this djangoAssignment project.

## Project Structure

```
root_folder/
│
├──propertiesManagement/
│   ├── media/
│   ├── properties/
│   │   ├── management/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── property_system/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── .gitignore
│   ├── config.py
│   ├── config.py.sample
│   ├── manage.py
│   ├── README.md
│   └── requirements.txt
│
├── scrapyAssignment/
```

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/noman62/propertiesManagement
   cd propertiesManagement
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration

1. Create a `config.py` file in the DjangoAssignment root directory and add your PostgreSQL credentials:

   ```python
   # config.py
   DB_USERNAME = 'your_username'
   DB_PASSWORD = 'your_password'
   DB_HOST = 'localhost'
   DB_PORT = 'port'
   DJANGO_DBNAME = 'django_project_database_name'
   SCRAPY_DBNAME = 'Scrapy_project_database_name'
   SECRET_KEY = 'your SECRET_KEY'
   ```

2. Ensure PostgreSQL is running and create the necessary databases:

   ```bash
   psql -U your_username
   CREATE DATABASE django_project_database_name;
   CREATE DATABASE Scrapy_project_database_name;
   ```

### Running the Application

1. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the admin panel at `http://localhost:8000/admin/` and log in with your superuser credentials.
2. Use the admin interface to manage properties, images, locations, and amenities.

## Database Schema

The project includes the following models:
- Property
- Image (One-to-Many with Property)
- Location (Many-to-Many with Property)
- Amenity (Many-to-Many with Property)

Each model includes fields as specified in the project requirements.

## CLI Data Migration

To migrate data from the Scrapy project database to Django:

```bash
python manage.py migrate_scrapy_data
```

This custom management command will transfer data from your Scrapy project's database to the Django application's database.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

[Specify the license for your project here]
