import sys
import requests

#Given Parameters
API_KEY = "f897a99d971b5eef57be6fafa0d83239"
#API_URL = "https://openweathermap.org/api/geocoding-api"
API_URL = "http://api.openweathermap.org/geo/1.0/"


def get_data_by_cityandstate(cityandstate):
    
    city, state = cityandstate.split(", ")
    url = f"{API_URL}direct?q={city},{state},USA&limit=1&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return{
            "name" : data.get("name"),
            "state" : data.get("state"),
            "lat" : data.get("lat"),
            "lon" : data.get("lon"),
            "country" : data.get("country")
        }
    else:
        return None


def get_data_by_zipcode(zipcode):
    #http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
    url = f"{API_URL}zip?zip={zipcode}&appid={API_KEY}"
    #print(f"url : ", url)
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()
        return{
            "name" : data.get("name"),
            "zip" : data.get("zip"),
            "lat" : data.get("lat"),
            "lon" : data.get("lon"),
            "country" : data.get("country")

        }
    else:
        return None
    

def get_data_from_multiple_locations(locations):
    results_data = []
    for location in locations:
        if "," in location:
            result_data = get_data_by_cityandstate(location)
        else:
            result_data = get_data_by_zipcode(location)
        
        if result_data:
            results_data.append(result_data)
        else:
            results_data.append({"error": f"Location Not Found : {location}"})

    return results_data
    
def main():
    if len(sys.argv) < 2:
        print ("Use: python openweathergeocoding.py <location1=City, State><location2=Zip>.....")
        sys.exit(1)

    locations = sys.argv[1:]
    results = get_data_from_multiple_locations(locations)

    for result in results:
        if "error" in result:
            print(result["error"])
        else:
             print(f"Name: {result.get('name')}, State: {result.get('state', 'N/A')}, "
                  f"Latitude: {result.get('lat')}, Longitude: {result.get('lon')}")


if __name__ == "__main__":
    main()
