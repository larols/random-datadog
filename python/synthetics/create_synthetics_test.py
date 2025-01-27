from datadog import initialize, api

# Initialize Datadog API and App keys
options = {
    "api_key": "your-api-key",
    "app_key": "your-app-key",
    "api_host": "https://api.datadoghq.eu",  # Specify the Datadog site
}

initialize(**options)

# Define the test details
synthetics_test_details = {
    "type": "api",
    "config": {
        "request": {
            "method": "GET",
            "url": "https://example.com",
            "timeout": 30,
        },
        "assertions": [
            {"type": "statusCode", "operator": "is", "target": 200},
            {"type": "responseTime", "operator": "lessThan", "target": 2000},
        ],
    },
    "locations": ["aws:us-east-1", "aws:eu-central-1"],
    "options": {
        "tick_every": 900,
        "retry": {
            "count": 2,
            "interval": 300,
        },
    },
    "message": "Synthetic test for example.com",
    "name": "Example HTTP Test",
    "tags": ["env:production", "team:devops"],
    "status": "live",
}

# Create the synthetic test
response = api.Synthetics.create_test(**synthetics_test_details)

# Output the response
print("Synthetic test created:")
print(response)