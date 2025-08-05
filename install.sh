#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if virtual environment folder exists
if [ ! -d ".env" ]; then
  echo "Creating config file..."
  touch .env
else
  echo "Config file already exists."
fi

# Check if virtual environment folder exists
if [ ! -d ".venv" ]; then
  echo "Creating Python virtual environment..."
  python3.11 -m venv .venv
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt -t hydration_reminder --no-cache-dir

# Get Twilio credentials, user's phone number and Google API key
read -p "TWILIO_ACCOUNT_SID: " TWILIO_ACCOUNT_SID
read -p "TWILIO_AUTH_TOKEN: " TWILIO_AUTH_TOKEN
read -p "TWILIO_PHONE_NUMBER, include country code, i.e. +34: " TWILIO_PHONE_NUMBER
read -p "TO_PHONE_NUMBER, include country code, i.e. +34: " TO_PHONE_NUMBER
read -p "GOOGLE_API_KEY: " GOOGLE_API_KEY

# Get AWS credentials to allow Terraform to create resources
read -p "AWS_ACCESS_KEY_ID: " AWS_ACCESS_KEY_ID
read -p "AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY

# Write credentials to .env file
echo "Writing credentials to .env file..."
echo "export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" >> .env
echo "export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" >> .env

# Creating infrastructure with Terraform
echo "Creating the infrastructure with Terraform..."
source .env
cd terraform
terraform init
terraform apply -auto-approve -var="twilio_account_sid=$TWILIO_ACCOUNT_SID" -var="twilio_auth_token=$TWILIO_AUTH_TOKEN" -var="twilio_phone_number=$TWILIO_PHONE_NUMBER" -var="to_phone_number=$TO_PHONE_NUMBER" -var="google_api_key=$GOOGLE_API_KEY"
cd ..
deactivate

# Setup complete
echo "Setup complete"
