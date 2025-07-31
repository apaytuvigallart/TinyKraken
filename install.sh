#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if virtual environment folder exists
if [ ! -d ".venv" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv .venv
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
pip install -r requirements.txt

# Create a sample .env file if it doesn't exist
if [ ! -f ".env" ]; then
  echo "Creating .env template file..."
  cat <<EOL > .env
# Replace these placeholders with your actual keys and numbers
TWILIO_ACCOUNT_SID="your_twilio_account_sid"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
TWILIO_PHONE_NUMBER="+1234567890"
TO_PHONE_NUMBER="+0987654321"
GEMINI_API_KEY="your_gemini_api_key"
EOL
  echo ".env file created. Please edit it with your credentials."
else
  echo ".env file already exists. Please ensure it contains the correct credentials."
fi

echo "Setup complete. Don't forget to activate the virtual environment with:"
echo "  source .venv/bin/activate"
echo "and fill in your .env file with the correct credentials."
