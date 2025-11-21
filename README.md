# Django Planets CRUD API

RESTful API for planets data. Fetches data from an external GraphQL API and provides full CRUD operations.

## Requirements

- Docker Desktop
- Docker Compose

## Quick Start

```bash
bash start.sh
```

The script will automatically:
- ✅ Build Docker images
- ✅ Start PostgreSQL database
- ✅ Run database migrations
- ✅ Load planet data from external API (60 planets)
- ✅ Start Django development server

**API available at:** http://localhost:8000/api/planets/  
**Swagger UI at:** http://localhost:8000/

## API Endpoints

- `GET /api/planets/` - List all planets (paginated, 20 per page)
- `GET /api/planets/{id}/` - Get planet details
- `POST /api/planets/` - Create a new planet
- `PUT /api/planets/{id}/` - Update planet (all fields)
- `PATCH /api/planets/{id}/` - Partial update
- `DELETE /api/planets/{id}/` - Delete planet

### Pagination

Results are paginated with 20 items per page. Use `?page=2` to navigate:

```bash
GET /api/planets/?page=1
GET /api/planets/?page=2
```

## Data Model

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

## Running Tests

```bash
# Run all tests
docker-compose exec web pytest

# Run with coverage
docker-compose exec web pytest --cov=planets

# Run specific test file
docker-compose exec web pytest planets/tests/test_api.py
```

## Logs

Application logs: `./logs/app.log`

## Environment Variables

The project uses environment variables configured in `docker-compose.yml`. For reference, see `.env.example` which lists all available variables:

- `DEBUG` - Django debug mode
- `PLANETS_URL` - External GraphQL API endpoint
- `DATABASE_*` - PostgreSQL connection settings

## Technology Stack

- Django 5.2.8 + Django REST Framework
- PostgreSQL 15
- Docker, Docker Compose
- pytest for testing
