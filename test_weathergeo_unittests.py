import unittest
from openweathergeocoding import get_data_by_cityandstate, get_data_by_zipcode


class TestGeoWeatherAPI(unittest.TestCase):
    def test_by_city_and_state(self):
        result_data = get_data_by_cityandstate("San Jose, CA")
        self.assertIsNotNone(result_data)
        print(f"city name: ", result_data["name"])
        assert result_data["name"] == "San Jose", "City does not match"
        print(f"state : ", result_data["state"])
        assert result_data["state"] == "California", "State does not match"
        print(f"lattitude : ", result_data["lat"])
        #self.assertEqual (result_data["lat"], 37.3361663, "Lattitude doesn't match")
        assert result_data["lat"] == 37.3361663, "Lattitude does not match"
        print(f"longitude : ", result_data["lon"])
        assert result_data["lon"] == -121.890591, "Longitude does not match"
        print(f"country : ", result_data["country"])
        assert result_data["country"] == "US", "Country does not match"

    def test_by_zip_code(self):
        result_data = get_data_by_zipcode("95148")
        self.assertIsNotNone(result_data)
        print(f"city name: ", result_data["name"])
        assert result_data["name"] == "San Jose", "City does not match"
        print(f"zip : ", result_data["zip"])
        assert result_data["zip"] == "95148", "Zip does not match"
        print(f"lattitude : ", result_data["lat"])
        #self.assertEqual (result_data["lat"], 37.3361663, "Lattitude doesn't match")
        assert result_data["lat"] == 37.3304, "Lattitude does not match"
        print(f"longitude : ", result_data["lon"])
        assert result_data["lon"] == -121.7913, "Longitude does not match"
        print(f"country : ", result_data["country"])
        assert result_data["country"] == "US", "Country does not match"



if __name__ == "__main__":
    unittest.main()