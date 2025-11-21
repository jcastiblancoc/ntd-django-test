# Django Planets CRUD API

RESTful API for planet data. It fetches data from an external GraphQL API and provides full CRUD operations.

---

## Explanation of the Project

This project provides a **RESTful API for planet data**, retrieving information from an external **GraphQL API** and exposing full CRUD operations.

The backend is built with:

- **Django 5.2.8**
- **Django REST Framework 3.16.1**

To ensure consistency and portability, the entire application runs inside **Docker** containers managed with **Docker Compose**, preventing environment-specific issues (including `.env` misconfiguration).

---

### Purpose

The goal is to deliver a fully containerized Django REST API configured through environment variables. Once the repository is cloned and the `start.sh` script is executed, the services will be available at:

- API endpoint: `http://localhost:8000/api/planets/`
- Swagger UI: `http://localhost:8000/`
- Application logs: `./logs/app.log`

---

### Features

- List planets (paginated, 20 per page)
- Retrieve planet details
- Create a new planet
- Update planet (full update)
- Apply partial update
- Delete a planet

---

### Additional Capabilities

- Load 60 planets from an external GraphQL API
- Run automated tests to validate the setup
- Start Django development server via script
- Generate automatic API documentation using **drf-spectacular** (Swagger UI)

---

### Quick Start

**Clone the repository and run the `start.sh` script.**  
It will build, start, test, and prepare the API automatically.

---

## Requirements

- Docker Desktop
- Docker Compose

---

## Quick Start Command

Run the following command in the root directory of the project:

```bash
./start.sh
```

If the script does not have execution permissions, use:

```bash
chmod +x start.sh
```

The script will automatically:

- Build Docker images
- Start PostgreSQL database
- Run database migrations
- Load planet data from the external API (60 planets)
- Run tests to validate setup
- Start the Django development server

**API available at:** http://localhost:8000/api/planets/  
**Swagger UI at:** http://localhost:8000/

---

## API Endpoints

- `GET /api/planets/` – List all planets (paginated, 20 per page)
- `GET /api/planets/{id}/` – Get planet details
- `POST /api/planets/` – Create a new planet
- `PUT /api/planets/{id}/` – Full update
- `PATCH /api/planets/{id}/` – Partial update
- `DELETE /api/planets/{id}/` – Delete a planet

### Pagination

Results are paginated with 20 items per page. Use `?page=2` to navigate:

```http
GET /api/planets/?page=1
GET /api/planets/?page=2
```

---

## Data Model (Example Response)

```json
{
  "id": 1,
  "name": "Earth",
  "population": "7800000000",
  "terrains": ["grasslands", "mountains"],
  "climates": ["temperate", "tropical"],
  "created_at": "2025-11-21T01:00:00Z"
}
```

---

## Logs

Application logs: `./logs/app.log`

---

## Environment Variables

The project uses environment variables from the `.env` file:

- `PLANETS_URL` – External GraphQL API endpoint
- `DATABASE_*` – PostgreSQL connection settings
- `POSTGRES_*` – PostgreSQL container configuration

---

## Technology Stack

- Django 5.2.8 + Django REST Framework
- PostgreSQL 15
- Docker, Docker Compose
- pytest for testing

---

## Author

**Jeisson Castiblanco Carrera**  
Backend Software Engineer  
castiblanco.jeisson@gmail.com

---

## Future Improvements

Possible enhancements to extend the functionality of this project:

### 1. Django Admin Interface

- Enable and customize the Django admin panel for easy data management
- Create custom admin views for Planet model with filters and search capabilities
- Add inline editing for related fields
- Implement custom actions for bulk operations

### 2. Web Frontend with Django Templates

- Build a complete web interface using Django templates
- Create pages for:
  - Planet list view with pagination
  - Planet detail page with all information
  - Forms for creating and editing planets
  - Search and filter functionality
- Add Bootstrap or Tailwind CSS for responsive design
- Implement HTMX for dynamic interactions without full page reloads

### 3. Additional Features

- Add user authentication and authorization
- Implement API rate limiting
- Create data export functionality (CSV, JSON, PDF)
- Implement CI/CD pipeline for automated testing and deployment
