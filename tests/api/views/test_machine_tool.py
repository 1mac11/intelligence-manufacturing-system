import os

from django.urls import reverse
from requests import Response

import pytest
from rest_framework.test import APIClient

from core.models.machine_tool_type import MachineToolTypeChoices
from tests.api.views import get_choice_list

current_dir = os.path.dirname(__file__)


class TestMachineToolType:
    @pytest.mark.django_db
    def test_machine_tool_type_list(self, client: APIClient):
        path = reverse('machinetooltype-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200

        choices = get_choice_list(MachineToolTypeChoices)
        for obj in response.json():
            assert obj['name'] in choices


class TestMachineTool:
    @pytest.mark.django_db
    def test_machine_tool_type_list(self, client: APIClient):
        path = reverse('machinetool-list')
        response: Response = client.get(path, follow=True)

        assert response.status_code == 200
