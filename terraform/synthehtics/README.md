Terraform Datadog Synthetics Test

This Terraform project sets up a Datadog Synthetics test using the Datadog provider.

Files Included
--------------
- main.tf: Defines the Terraform configuration.
- variables.tf: Specifies variables for the configuration.
- terraform.tfvars: Stores variable values.

Prerequisites
-------------
- Terraform CLI installed (https://www.terraform.io/downloads)
- A Datadog account with API and application keys
- API URL (e.g., https://api.datadoghq.com for US or https://api.datadoghq.eu for EU)

Instructions
------------
1. Configuration
   - Populate the terraform.tfvars file with your credentials:
     ```
     datadog_api_key = "your-api-key"
     datadog_app_key = "your-app-key"
     datadog_api_url = "https://api.datadoghq.eu" # Change to your region
     ```

   - Alternatively, remove terraform.tfvars and set variables using environment variables:
     ```
     export TF_VAR_datadog_api_key="your-api-key"
     export TF_VAR_datadog_app_key="your-app-key"
     export TF_VAR_datadog_api_url="https://api.datadoghq.eu"
     ```

2. Commands
   - Initialize Terraform:
     ```
     terraform init
     ```

   - View the execution plan:
     ```
     terraform plan
     ```

   - Apply the changes:
     ```
     terraform apply
     ```

   - Delete the resources:
     ```
     terraform destroy
     ```

Notes
-----
- Ensure you have the correct permissions in your Datadog account for creating Synthetics tests.
- For further customization, modify the variables in variables.tf or the configuration in main.tf.
