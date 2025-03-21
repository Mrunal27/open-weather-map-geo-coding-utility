# Open Weather Map Geo Coding Utility

This utility retrieves City Name, State, latitude, longitude, Country, Zip Code information for a given city/state or zip code using the OpenWeather Geocoding API.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Mrunal27/open-weather-map-geo-coding-utility.git
   cd open-weather-map-geo-coding-utility
2. Install Dependencies
    pip install -r requirements.txt

## Running Instruction
1. In command prompt run using the following command
   ```bash
     python .\openweathergeocoding.py "San Jose, CA", "95050", "94087", "00000", "ABCDEF", " "
     Name: San Jose, State: California, Latitude: 37.3361663, Longitude: -121.890591
     Name: Santa Clara, State: N/A, Latitude: 37.3492, Longitude: -121.953
     Name: Sunnyvale, State: N/A, Latitude: 37.3502, Longitude: -122.0349
     Location Not Found : 00000
     Location Not Found : ABCDEF
     Location Not Found :     
     
2. Running a test file
    python .\test_weathergeo_utility_integration.py

    Output looks like the following
    ...STDOUT: Location Not Found : ABCDERFG

    STDERR: 
   .STDOUT: Location Not Found : #124@@~!

   STDERR: 
   ..
   ----------------------------------------------------------------------
   Ran 6 tests in 2.569s

   OK
   
