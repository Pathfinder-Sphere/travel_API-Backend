import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from the environment variable
aviationstack_api_key = os.getenv('AVIATIONSTACK_API_KEY')

params = {
  'access_key': aviationstack_api_key,
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
print(api_response)

with open('response.json', 'w') as f:
    f.write(str(api_response))

# for flight in api_response['results']:
#     if (flight['live']['is_ground'] is False):
#         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
#             flight['airline']['name'],
#             flight['flight']['iata'],
#             flight['departure']['airport'],
#             flight['departure']['iata'],
#             flight['arrival']['airport'],
#             flight['arrival']['iata']))