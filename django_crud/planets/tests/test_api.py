import pytest
from rest_framework.test import APIClient
from rest_framework import status
from planets.models import Planet


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_planet():
    return Planet.objects.create(
        name="Tatooine",
        population="200000",
        terrains=["desert"],
        climates=["arid"]
    )


@pytest.mark.django_db
class TestPlanetAPI:
    
    def test_list_planets(self, api_client):
        Planet.objects.create(name="Earth", population="7800000000")
        Planet.objects.create(name="Mars", population="unknown")
        
        response = api_client.get('/api/planets/')
        
        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data
        assert len(response.data['results']) == 2
    
    def test_retrieve_planet(self, api_client, sample_planet):
        response = api_client.get(f'/api/planets/{sample_planet.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Tatooine"
        assert response.data['population'] == "200000"
    
    def test_create_planet(self, api_client):
        data = {
            "name": "Naboo",
            "population": "4500000000",
            "terrains": ["grassy hills"],
            "climates": ["temperate"]
        }
        
        response = api_client.post('/api/planets/', data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == "Naboo"
        assert Planet.objects.filter(name="Naboo").exists()
    
    def test_update_planet(self, api_client, sample_planet):
        data = {
            "name": "Tatooine",
            "population": "250000",
            "terrains": ["desert"],
            "climates": ["arid"]
        }
        
        response = api_client.put(
            f'/api/planets/{sample_planet.id}/',
            data,
            format='json'
        )
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['population'] == "250000"
    
    def test_partial_update_planet(self, api_client, sample_planet):
        data = {"population": "300000"}
        
        response = api_client.patch(
            f'/api/planets/{sample_planet.id}/',
            data,
            format='json'
        )
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['population'] == "300000"
    
    def test_delete_planet(self, api_client, sample_planet):
        planet_id = sample_planet.id
        
        response = api_client.delete(f'/api/planets/{planet_id}/')
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Planet.objects.filter(id=planet_id).exists()
