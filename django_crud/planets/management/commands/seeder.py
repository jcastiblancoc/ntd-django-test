import os
import logging
import requests
from django.core.management.base import BaseCommand
from planets.models import Planet

logger = logging.getLogger('planets')


class Command(BaseCommand):
    help = "Load planets from external API"

    def handle(self, *args, **kwargs):
        url = os.getenv("PLANETS_URL")
        
        logger.info("Starting seeder command")
        logger.info(f"Fetching planets from: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            logger.info(f"API response status: {response.status_code}")
            
            data = response.json()
            planets = data["data"]["allPlanets"]["planets"]
            
            logger.info(f"Found {len(planets)} planets to process")
            
            created_count = 0
            updated_count = 0
            
            for p in planets:
                planet, created = Planet.objects.update_or_create(
                    name=p.get("name"),
                    defaults={
                        "population": p.get("population"),
                        "terrains": p.get("terrains"),
                        "climates": p.get("climates"),
                    },
                )
                if created:
                    created_count += 1
                    logger.debug(f"Created planet: {planet.name}")
                else:
                    updated_count += 1
                    logger.debug(f"Updated planet: {planet.name}")
            
            logger.info(f"Seeder completed: {created_count} created, {updated_count} updated")
            self.stdout.write(f"Loaded {len(planets)} planets")
            
        except Exception as e:
            logger.error(f"Seeder failed: {str(e)}", exc_info=True)
            self.stdout.write(f"Error: {str(e)}")
    


