import json
import sys
from datadog import initialize, api

# Initialize Datadog API and App keys
options = {
    "api_key": "your-api-key",
    "app_key": "your-app-key",
    "api_host": "https://api.datadoghq.eu",
}

initialize(**options)

def import_test(input_file):
    """Read a JSON file and create/update a synthetic test in Datadog."""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            test_data = json.load(f)

        # Remove unnecessary fields before re-importing
        for field in ["public_id", "created_at", "modified_at", "creator", "monitor_id"]:
            test_data.pop(field, None)  # Safely remove fields if they exist

        response = api.Synthetics.create_test(**test_data)
        
        if "errors" in response:
            print(f"Error creating test: {response['errors']}")
        else:
            print(f"Test created with ID: {response['public_id']}")

    except Exception as e:
        print(f"Failed to import test: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_synthetic_test.py <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    import_test(input_file)