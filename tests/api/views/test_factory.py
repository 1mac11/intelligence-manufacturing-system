import os

from django.urls import reverse
from requests import Response

import pytest
from rest_framework.test import APIClient

from core.models.factory_type import FactoryTypeChoices
from tests.api.views import get_choice_list

current_dir = os.path.dirname(__file__)


class TestFactoryType:
    @pytest.mark.django_db
    def test_factory_type_list(self, client: APIClient):
        path = reverse('factorytype-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200

        choices = get_choice_list(FactoryTypeChoices)
        for factory_type in response.json():
            assert factory_type['name'] in choices


class TestFactory:
    @pytest.mark.django_db
    def test_factory_list(self, client: APIClient):
        path = reverse('factory-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200
