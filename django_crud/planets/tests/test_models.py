import pytest
from django.db import IntegrityError
from planets.models import Planet


@pytest.mark.django_db
class TestPlanetModel:
    
    def test_create_planet(self):
        planet = Planet.objects.create(
            name="Earth",
            population="7800000000",
            terrains=["grasslands", "mountains"],
            climates=["temperate", "tropical"]
        )
        
        assert planet.id is not None
        assert planet.name == "Earth"
        assert planet.population == "7800000000"
        assert planet.created_at is not None
    
    def test_unique_name_constraint(self):
        Planet.objects.create(name="Venus")
        
        with pytest.raises(IntegrityError):
            Planet.objects.create(name="Venus")
