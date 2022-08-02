import os

from django.urls import reverse
from requests import Response

import pytest
from rest_framework.test import APIClient

from core.models import BuildingTypeChoices
from tests.api.views import get_choice_list


class TestBuildingType:
    @pytest.mark.django_db
    def test_building_type_list(self, client: APIClient):
        path = reverse('buildingtype-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200

        choices = get_choice_list(BuildingTypeChoices)
        for obj in response.json():
            assert obj['name'] in choices


class TestBuilding:
    @pytest.mark.django_db
    def test_building_list(self, client: APIClient):
        path = reverse('building-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200
