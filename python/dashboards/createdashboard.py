import requests
import json

# Prompt the user to enter the API and Application keys
api_key = input("Please enter your Datadog API key: ")
app_key = input("Please enter your Datadog Application key: ")

# Prompt the user to enter the filename
filename = input("Please enter the JSON file name: ")

# Read the JSON file
with open(filename, 'r') as file:
    dashboard_data = json.load(file)

# Prompt the user for a new dashboard name
new_dashboard_name = input("Please enter the new dashboard name: ")

# Update the dashboard title in the JSON data
dashboard_data['title'] = new_dashboard_name

# URL to create the dashboard
url = 'https://api.datadoghq.com/api/v1/dashboard'

# Headers including the API and Application keys
headers = {
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key,
    'Content-Type': 'application/json'
}

# Make the POST request to create the dashboard
response = requests.post(url, headers=headers, data=json.dumps(dashboard_data))

# Check if the request was successful
if response.status_code == 200:
    print("Dashboard created successfully")
else:
    print(f"Failed to create dashboard: {response.status_code}")
    print(response.text)

