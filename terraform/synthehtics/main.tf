terraform {
  required_providers {
    datadog = {
      source  = "DataDog/datadog"
      version = "~> 3.53.0"
    }
  }
}

provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
  api_url = var.datadog_api_url
}

resource "datadog_synthetics_test" "example_http_test" {
  name      = "Example HTTP Test"
  type      = "api"
  subtype   = "http"

  request_definition {
    method  = "GET"
    url     = "https://example.com"
    timeout = 30
  }

  assertion {
    type     = "statusCode"
    operator = "is"
    target   = 200
  }

  assertion {
    type     = "responseTime"
    operator = "lessThan"
    target   = 2000
  }

  locations = ["aws:us-east-1", "aws:eu-central-1"]
  status    = "live"
  tags      = ["env:production", "team:devops"]

  options_list {
    tick_every = 900
    retry {
      count    = 2
      interval = 300
    }
  }
}