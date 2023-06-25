from django.test import TestCase
import requests

# Define the URL for the create rating endpoint
url = 'http://localhost:8000/ratings/'

# Define the data for the rating
data = {
    'user': 1,  # ID of the user
    'book': 1,  # ID of the book
    'rating': 4  # Rating value
}

# Send the POST request to create the rating
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 201:
    print("Rating created successfully!")
else:
    print("Failed to create rating. Error:", response.text)
# Create your tests here.
