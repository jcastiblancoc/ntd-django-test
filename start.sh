#!/bin/bash

set -e

# Create logs directory
LOGS_DIR="./logs"
mkdir -p "$LOGS_DIR"

# Single log file for all logs
LOG_FILE="$LOGS_DIR/app.log"

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

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
docker-compose down &> /dev/null || docker compose down &> /dev/null || true

# Build and start
echo "Building Docker images..."
log "STARTUP: Building Docker images"
docker-compose build &> /dev/null || docker compose build &> /dev/null
log "STARTUP: Docker images built successfully"

echo "Starting services..."
log "STARTUP: Starting Docker services"
docker-compose up -d &> /dev/null || docker compose up -d &> /dev/null
log "STARTUP: Services started successfully"

# Wait for services
echo "Waiting for services to be ready..."
sleep 10

# Run seeder automatically
echo "Loading planet data..."
log "SEEDER: Starting seeder command"
docker-compose exec web python manage.py seeder 2>&1 | grep -E "(Starting|Found|completed|Loaded|Error)" | while read line; do
    log "SEEDER: $line"
done || docker compose exec web python manage.py seeder 2>&1 | grep -E "(Starting|Found|completed|Loaded|Error)" | while read line; do
    log "SEEDER: $line"
done

echo ""
echo "=========================================="
echo "SUCCESS: API is running"
echo "=========================================="
echo ""
echo "Swagger UI:  http://localhost:8000/"
echo "API:         http://localhost:8000/api/planets/"
echo "Logs:        $LOG_FILE"
echo ""
echo "Useful commands:"
echo "  View logs:   docker-compose logs -f web"
echo "  Stop:        docker-compose down"
echo "  Restart:     docker-compose restart web"
echo ""
