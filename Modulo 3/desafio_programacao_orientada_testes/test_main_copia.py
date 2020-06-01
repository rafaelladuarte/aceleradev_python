from main_copia import get_temperature
from unittest import TestCase
from unittest.mock import patch
import pytest

expected = 16
temperature = 62
parametrized_values = [(expected, temperature)]


@pytest.mark.parametrize("expected,temperature", parametrized_values)
class Test(TestCase):
    testID = ""
    errors = []
    temperature_dict = {}

    @patch.dict(temperature_dict, {"currently": {"temperature": temperature}})
    def test_get_temperature_by_lat_lng(self):
        lat = -14.235004
        lng = -51.92528

        patcher = patch('main_copia.requests.get')
        temperature_dict = {"currently": {"temperature": temperature}}

        mock = patcher.start()
        mock.return_value.json.return_value = temperature_dict
        result = get_temperature(lat, lng)
        mock.stop()

        if result != expected:
            Test.errors.append("failed: " + Test.testID)

        with patch.dict(temperature_dict, {'currently': {'temperature': expected}}):
            self.assertEqual(result, expected)