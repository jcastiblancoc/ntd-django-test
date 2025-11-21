# Django Planets CRUD

Simple RESTful API for planets data.

## Requirements

- Docker
- Docker Compose

## Quick Start

```bash
./start.sh
```

That's it! The script will:
- Build Docker images
- Start PostgreSQL database
- Run migrations
- Load planet data from external API
- Start Django server

API will be available at: http://localhost:8000/api/planets/

## API Endpoints

- `GET /api/planets/` - List all planets
- `POST /api/planets/` - Create a planet
- `GET /api/planets/{id}/` - Get a planet
- `PUT /api/planets/{id}/` - Update a planet (all fields required)
- `PATCH /api/planets/{id}/` - Partial update (only fields provided)
- `DELETE /api/planets/{id}/` - Delete a planet

## Swagger UI

Interactive API documentation available at: http://localhost:8000/

## Useful Commands

```bash
# View logs
docker-compose logs -f web

# Stop services
docker-compose down

# Restart
docker-compose restart web

# Load data again
docker-compose exec web python manage.py seeder
```
