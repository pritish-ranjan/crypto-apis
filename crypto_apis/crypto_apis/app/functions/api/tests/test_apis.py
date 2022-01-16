from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

def test_initialize_pytest():
    assert 1 == 1

def test_successfully_extract_coinbase_data():
        mock_raise_request = create_patch(
            "extract.main.Extract.main"
        )
        mock_raise_request.return_value = [
                                            [
                                                1634555040,
                                                61083.95,
                                                61301.27,
                                                61123.4,
                                                61281.36,
                                                20.28026853
                                            ],
                                            [
                                                1634554980,
                                                61107.99,
                                                61184.67,
                                                61121.84,
                                                61125.63,
                                                14.52609662
                                            ]
                                        ]
        client = APIClient()
        url = reverse("api:btc-usd-rate-extract")

        response_data = "Record created in the database Historical table!"

        response = client.get(url, format="json")

        assertEqual(response.status_code, status.HTTP_200_OK)
        assertEqual(response.data, response_data)

