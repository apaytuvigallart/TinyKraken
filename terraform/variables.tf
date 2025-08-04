variable "common_tags" {
  description = "Common tags to be applied to all resources"
  type        = map(string)
  default = {
    Project   = "TinyKraken"
    ManagedBy = "Terraform"
  }
}
