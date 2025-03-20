import unittest
import subprocess
import json

class TestOpenWeatherMapGeoCodingUtility(unittest.TestCase):
    
    def test_by_city_and_state(self):
        result = subprocess.run(
            ["python", "openweathergeocoding.py", "San Jose, CA"],
            capture_output=True, text=True, shell=True
        )
        format_string = result.stdout.strip()
        pairs = format_string.split(", ")
        print("pairs ", pairs)
        resulted_data = {}
        for pair in pairs:
            key, value = pair.split(": ")
            resulted_data[key] = value
        
        assert resulted_data["Name"] == "San Jose", "City Name is Not Matching"
        assert resulted_data["State"] == "California", "State Name is Not Matching"
        assert resulted_data["Latitude"] == "37.3361663", "Latitude is Not Matching"
        assert resulted_data["Longitude"] == "-121.890591", "Longitude is Not Matching"
    
    def test_by_zip_code(self):
        result = subprocess.run(
            ["python", "openweathergeocoding.py", "95148"],
            capture_output=True, text=True, shell=True
        )
        
        resulted_data = result.stdout.strip()
        self.assertIn("Name: San Jose", resulted_data)
        self.assertIn("Latitude:", resulted_data)
        self.assertIn("Longitude:", resulted_data)
        
    def test_by_multiple_locations(self):
        result = subprocess.run(
            ["python", "openweathergeocoding.py", "San Jose, CA", "95148", "Santa Clara, CA", "95050"],
            capture_output=True, text=True, shell=True
        )
        format_string = result.stdout.strip()
        pairs = format_string.split(", ")
        print("pairs ", pairs)
        resulted_data = result.stdout.strip()
        #Checking for State and City Combination
        self.assertIn("Name: San Jose", resulted_data)
        self.assertIn("State: California", resulted_data)
        self.assertIn("Name: Santa Clara", resulted_data)
        self.assertIn("State: California", resulted_data)
       
        #Checking for ZipCode
        self.assertIn("Name: San Jose", resulted_data)
        self.assertIn("Latitude:", resulted_data)
        self.assertIn("Longitude:", resulted_data)
        self.assertIn("Name: Santa Clara", resulted_data)
        
    
    def test_no_input(self):
        #Testing the utility has no input, handling null values
        result = subprocess.run(
            ["python", "openweathergeocoding.py"],
            capture_output=True, text=True, shell=True
        )
        resulted_data = result.stdout.strip()
        #Checking for No Input
        self.assertIn("Use: python openweathergeocoding.py <location1=City, State><location2=Zip>.....", resulted_data)

    
    def test_invalid_input(self):
        result = subprocess.run(
            ["python", "openweathergeocoding.py", "ABCDERFG"],
            capture_output=True, text=True, shell=True
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertIn("Location Not Found : ABCDERFG", result.stdout.strip())

    
    def test_invalid_zip_code(self):
        result = subprocess.run(
            ["python", "openweathergeocoding.py", "#124@@~!"],
            capture_output=True, text=True, shell=True
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertIn("Location Not Found : #124@@~!", result.stdout.strip())
    
        


if __name__ == "__main__":
    unittest.main()

