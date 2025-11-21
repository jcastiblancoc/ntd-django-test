import os
import requests
from django.core.management.base import BaseCommand
from planets.models import Planet


class Command(BaseCommand):
    help = "Load planets from external API"

    def handle(self, *args, **kwargs):
        url = os.getenv("PLANETS_URL")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            planets = data["data"]["allPlanets"]["planets"]
            
            for p in planets:
                Planet.objects.update_or_create(
                    name=p.get("name"),
                    defaults={
                        "population": p.get("population"),
                        "terrains": p.get("terrains"),
                        "climates": p.get("climates"),
                    },
                )
            
            self.stdout.write(f"Loaded {len(planets)} planets")
            
        except Exception as e:
            self.stdout.write(f"Error: {str(e)}")
    


