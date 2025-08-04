#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if virtual environment folder exists
if [ ! -d ".venv" ]; then
  echo "Creating Python virtual environment..."
  python3.11 -m venv .venv
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
sleep 5
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt --no-cache-dir

# Package the Python dependencies into a zip file
echo "Packaging Python dependencies into tiny_kraken.zip..."
deactivate
cd .venv/lib/python3.11/site-packages
zip -r ../../../../tiny_kraken.zip .

# Add the Python files to the zip file
echo "Adding Python files to tiny_kraken.zip..."
cd ../../../../
zip -j tiny_kraken.zip hydration_reminder/*.py

# Create a sample .env file if it doesn't exist
if [ ! -f ".env" ]; then
  read -p "TWILIO_ACCOUNT_SID: " TWILIO_ACCOUNT_SID
  read -p "TWILIO_AUTH_TOKEN: " TWILIO_AUTH_TOKEN
  read -p "TWILIO_PHONE_NUMBER, include country code, i.e. +34: " TWILIO_PHONE_NUMBER
  read -p "TO_PHONE_NUMBER, include country code, i.e. +34: " TO_PHONE_NUMBER
  read -p "GOOGLE_API_KEY: " GOOGLE_API_KEY

  echo "Creating .env template file..."
  cat <<EOL > .env
TWILIO_ACCOUNT_SID="$TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="$TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER="$TWILIO_PHONE_NUMBER"
TO_PHONE_NUMBER="$TO_PHONE_NUMBER"
GOOGLE_API_KEY="$GOOGLE_API_KEY"
EOL
  echo ".env file created."
else
  echo ".env file already exists. Please ensure it contains the correct credentials."
fi

echo "Setup complete. Don't forget to activate the virtual environment with:"
echo "  source .venv/bin/activate"
