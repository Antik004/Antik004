import requests

# Replace with your actual API URL
api_url = 'https://tryhackme.com/api/v2/badges/public-profile?userPublicId=3970366'

# Send GET request to the API
response = requests.get(api_url)

# Debugging: Print status code and raw response text
print("Response status code:", response.status_code)
print("Response content:", response.text)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Try to parse the response as JSON
        data = response.json()
        print("Parsed data:", data)
    except requests.exceptions.JSONDecodeError:
        # Handle JSON parsing error if the response is not JSON
        print("Failed to decode JSON. Response is:", response.text)
        exit(1)
else:
    # If the API request fails, print the error message
    print(f"API request failed with status code {response.status_code}")
    exit(1)
