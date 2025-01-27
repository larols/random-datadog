datadog_api_key = "your-api-key" # Replace with your actual Datadog API key
datadog_app_key = "your-app-key" # Replace with your actual Datadog Application key
datadog_api_url = "https://api.datadoghq.eu" # Override default site; remove this line or change to your Datadog site (e.g., "https://api.datadoghq.com" for the US site).

# Alternatively, you can remove this `terraform.tfvars` file and set the variables directly using environment variables:
# export TF_VAR_datadog_api_key="your-api-key"
# export TF_VAR_datadog_app_key="your-app-key"
# export TF_VAR_datadog_api_url="https://api.datadoghq.eu" # Or "https://api.datadoghq.com" for the US site.
