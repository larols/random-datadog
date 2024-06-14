import requests
import json

# Prompt the user to enter the API and Application keys
api_key = input("Please enter your Datadog API key: ")
app_key = input("Please enter your Datadog Application key: ")

# Prompt the user to enter the dashboard ID
dashboard_id = input("Please enter the dashboard ID: ")

# URL to fetch the dashboard
url = f'https://api.datadoghq.com/api/v1/dashboard/{dashboard_id}'

# Headers including the API and Application keys
headers = {
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make the GET request to fetch the dashboard
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    dashboard = response.json()
    
    # Get the dashboard name and use it to create a filename
    dashboard_name = dashboard.get('title', 'dashboard').replace(' ', '_')
    filename = f"{dashboard_name}.json"
    
    # Save the dashboard details to a file
    with open(filename, 'w') as file:
        json.dump(dashboard, file, indent=4)
    
    print(f"Dashboard details saved to {filename}")
else:
    print(f"Failed to fetch dashboard: {response.status_code}")
    print(response.text)

