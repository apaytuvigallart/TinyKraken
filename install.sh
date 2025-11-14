#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if virtual environment folder exists
if [[ ! -f ".env" ]]; then
  echo "Creating config file..."
  touch .env
else
  echo ".env file already exists."
fi

# Check if virtual environment folder exists
if [[ ! -d ".venv" ]]; then
  echo "Creating Python virtual environment..."
  python3.11 -m venv .venv
else
  echo "Virtual environment .venv already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install -q --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
mkdir -p python
pip install -q -r requirements.txt -t python --no-cache-dir --upgrade
zip -r -q python.zip python/

# Get Twilio credentials, user's phone number and Google API key
echo "Please enter the following credentials. Input is hidden for security reasons."
read -sp "TWILIO_ACCOUNT_SID: " TWILIO_ACCOUNT_SID; echo
read -sp "TWILIO_AUTH_TOKEN: " TWILIO_AUTH_TOKEN; echo
read -sp "TWILIO_PHONE_NUMBER, include country code, i.e. +34: " TWILIO_PHONE_NUMBER; echo
read -sp "TO_PHONE_NUMBER, include country code, i.e. +34: " TO_PHONE_NUMBER; echo
read -sp "GOOGLE_API_KEY: " GOOGLE_API_KEY; echo

# Get AWS credentials to allow Terraform to create resources
echo "Please enter your AWS credentials. Input is hidden for security reasons."
read -sp "AWS_ACCESS_KEY_ID: " AWS_ACCESS_KEY_ID; echo
read -sp "AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY; echo

# Write credentials to .env file
echo "Writing credentials to .env file..."
echo "export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" >> .env
echo "export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" >> .env

# Creating infrastructure with Terraform
echo "Creating the infrastructure with Terraform..."
source .env
cd infrastructure
terraform init
terraform apply -auto-approve -var="twilio_account_sid=$TWILIO_ACCOUNT_SID" -var="twilio_auth_token=$TWILIO_AUTH_TOKEN" -var="twilio_phone_number=$TWILIO_PHONE_NUMBER" -var="to_phone_number=$TO_PHONE_NUMBER" -var="google_api_key=$GOOGLE_API_KEY"
cd ..
deactivate

# Cleanup
echo "Cleaning up..."
rm -rf python
rm -rf .env
rm -rf .venv
rm -rf python.zip tiny_kraken_api.zip tiny_kraken_hydration_reminder.zip

# Setup complete
echo "Setup complete"
