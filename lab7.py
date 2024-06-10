import googlemaps
import requests
import json

def get_hotels(city):
    api_key = 'YOUR_GOOGLE_PLACES_API_KEY'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query=hotels+in+{city}&key={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        hotels = data['results']
        hotel_list = []
        
        for hotel in hotels:
            hotel_info = {
                'name': hotel['name'],
                'address': hotel['formatted_address'],
                'rating': hotel.get('rating', 'N/A'),
                'reviews': hotel.get('user_ratings_total', 'N/A')
            }
            hotel_list.append(hotel_info)
        
        return hotel_list
    else:
        return "No hotels found for this city."

city = input("Enter the name of the city: ")
result = get_hotels(city)

if isinstance(result, list):
    for hotel in result:
        print(f"Name: {hotel['name']}")
        print(f"Address: {hotel['address']}")
        print(f"Rating: {hotel['rating']}")
        print(f"Number of reviews: {hotel['reviews']}")
        print("------------------------------------")
else:
    print(result)
