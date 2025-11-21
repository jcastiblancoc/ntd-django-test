import pytest
from unittest.mock import patch, MagicMock
from django.core.management import call_command
from planets.models import Planet


@pytest.mark.django_db
class TestSeederCommand:
    
    @patch('planets.management.commands.seeder.requests.get')
    def test_seeder_loads_planets(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "allPlanets": {
                    "planets": [
                        {
                            "name": "Tatooine",
                            "population": "200000",
                            "terrains": ["desert"],
                            "climates": ["arid"]
                        },
                        {
                            "name": "Alderaan",
                            "population": "2000000000",
                            "terrains": ["grasslands"],
                            "climates": ["temperate"]
                        }
                    ]
                }
            }
        }
        mock_get.return_value = mock_response
        
        call_command('seeder')
        
        assert Planet.objects.count() == 2
        assert Planet.objects.filter(name="Tatooine").exists()
