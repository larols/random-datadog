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

def export_test(test_id, output_file):
    """Fetch a Datadog synthetic test and save it as a JSON file."""
    try:
        test = api.Synthetics.get_test(test_id)
        if "errors" in test:
            print(f"Error fetching test: {test['errors']}")
            return

        # Save test as JSON
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(test, f, indent=4)

        print(f"Test {test_id} exported to {output_file}")

    except Exception as e:
        print(f"Failed to export test: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_test.py <test_id> <output_file.json>")
        sys.exit(1)

    test_id = sys.argv[1]
    output_file = sys.argv[2]
    export_test(test_id, output_file)
