variable "common_tags" {
  description = "Common tags to be applied to all resources"
  type        = map(string)
  default = {
    Project   = "TinyKraken"
    ManagedBy = "Terraform"
  }
}

variable "twilio_account_sid" {
  description = "Twilio Account SID"
  type        = string
  sensitive   = true
}

variable "twilio_auth_token" {
  description = "Twilio Auth Token"
  type        = string
  sensitive   = true

}

variable "twilio_phone_number" {
  description = "Twilio Phone Number"
  type        = string
  sensitive   = true

}

variable "to_phone_number" {
  description = "To Phone Number"
  type        = string
  sensitive   = true

}

variable "google_api_key" {
  description = "Google API Key"
  type        = string
  sensitive   = true

}
