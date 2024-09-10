import requests
import sys
import urllib.parse

API_KEY = 'f897a99d971b5eef57be6fafa0d83239'


def get_location_by_name(location_name):
    encoded_location_name = urllib.parse.quote(location_name)
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={encoded_location_name}&limit=1&appid={API_KEY}'
    print(f'Requesting URL: {url}')
    response = requests.get(url)
    data = response.json()
    print(f'Response Data: {data}')
    if data:
        location = data[0]
        return {
            'place_name': location.get('name'),
            'latitude': location.get('lat'),
            'longitude': location.get('lon'),
            'country': location.get('country'),
            'state': location.get('state', 'N/A')
        }
    else:
        print(f'No data found for {location_name}')
        return None


def get_location_by_zip(zip_code):
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={API_KEY}'
    print(f'Requesting URL: {url}')
    response = requests.get(url)
    data = response.json()
    print(f'Response Data: {data}')
    if 'zip' in data:
        return {
            'place_name': data.get('name'),
            'latitude': data.get('lat'),
            'longitude': data.get('lon'),
            'country': data.get('country')
        }
    else:
        print(f'No data found for ZIP code {zip_code}')
        return None


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python geoloc_util.py <location1> <zip1> <location2> <zip2>")
        sys.exit(1)

    location1, zip1, location2, zip2 = sys.argv[1:5]

    print(f'Fetching data for: {location1}')
    location1_data = get_location_by_name(location1)
    if location1_data:
        print(f'{location1}: {location1_data}')

    print(f'Fetching data for ZIP code: {zip1}')
    zip1_data = get_location_by_zip(zip1)
    if zip1_data:
        print(f'{zip1}: {zip1_data}')

    print(f'Fetching data for: {location2}')
    location2_data = get_location_by_name(location2)
    if location2_data:
        print(f'{location2}: {location2_data}')

    print(f'Fetching data for ZIP code: {zip2}')
    zip2_data = get_location_by_zip(zip2)
    if zip2_data:
        print(f'{zip2}: {zip2_data}')
