#!/bin/bash

set -e

echo "Starting Django Planets API..."
echo ""

# Check Docker
if ! docker info &> /dev/null; then
    echo "ERROR: Docker is not running"
    echo "Please start Docker Desktop and try again"
    exit 1
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "ERROR: Docker Compose is not installed"
    echo "Please install Docker Compose"
    exit 1
fi

# Stop existing containers
echo "Stopping existing containers..."
docker-compose down 2>/dev/null || docker compose down 2>/dev/null || true

# Build and start
echo "Building Docker images..."
docker-compose build || docker compose build

echo "Starting services..."
docker-compose up -d || docker compose up -d

# Wait for services
echo "Waiting for services to be ready..."
sleep 10

# Run seeder automatically
echo "Loading planet data..."
docker-compose exec web python manage.py seeder 2>/dev/null || docker compose exec web python manage.py seeder 2>/dev/null

echo ""
echo "=========================================="
echo "SUCCESS: API is running"
echo "=========================================="
echo ""
echo "Swagger UI:  http://localhost:8000/"
echo "API:         http://localhost:8000/api/planets/"
echo ""
echo "Useful commands:"
echo "  View logs:   docker-compose logs -f web"
echo "  Stop:        docker-compose down"
echo "  Restart:     docker-compose restart web"
echo ""
