# TinyKraken 🐙
TinyKraken is a lightweight personal tool that sends SMS reminders to help you stay hydrated throughout the day. If you're the kind of person who forgets to drink water (like me), TinyKraken has your back — one message at a time.

## 🧠 What Does It Do?
TinyKraken sends a simple SMS message to your phone reminding you to drink water every weekday at 10:00 UTC. Messages are generated using **Gemini AI** to make them less repetitive or more encouraging. Messages are stored to DynamoDB for tracking purposes.

## 📦 Pre-requisites

- A **Twilio account** (to buy a phone number and send SMS notifications). 
- A **Gemini AI API key** (for message generation).
- Terraform. Please, follow this [documentation](https://developer.hashicorp.com/terraform/install) to install Terraform based on your OS.
- **AWS Account** to create an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to allow Terraform create the infrastructure.

## ☁️ API Setup

### 🔹 Twilio (for sending SMS)

1. **Create a Twilio Account**: Here is the [Console](https://console.twilio.com/).
2. **Free Trial**: New accounts receive **$15 in credits**, enough for basic usage.
3. **Buy a Phone Number**: Required to send messages.
4. **Grab Your Credentials** and keep them close, they're required for the installation:
   - Account SID.
   - Auth Token.
   - Twilio Phone Number.
   - Your Phone Number.

### 🔹 Gemini AI (for generating/personalizing messages)

1. Simply follow this [documentation](https://ai.google.dev/gemini-api/docs/api-key) to create a key for free.

### 🔹 Terraform (for building the infrastructure)
1. Simply make sure that Terraform is installed. Follow this [documentation](https://developer.hashicorp.com/terraform/install) to install Terraform.

### 🔹 AWS (for hosting both the infrastructure and the code)
1. Simply follow this [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys-admin-managed.html#admin-create-access-key) to create an access key for your user.

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/TinyKraken.git
cd TinyKraken
```

### 2. Run the install script
```bash
./install.sh
```
This script does the following:
- Creates `.env`, if it doesn't exist.
- Creates and activates `.venv` if it doesn't exist.
- Upgrades `pip` and then, it installs the dependencies from `requirements.txt`.
- Asks to set up the Environment Variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`
   - `TO_PHONE`
   - `GOOGLE_API_KEY`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
 - Writes the AWS credentials to `.env`. This will allow Terraform to create the infrastructure by using the credentials.
 - Creates the infrastructure to AWS.

## 🔥 How To Use It
Right now, AWS EventBridge Scheduler is scheduled to invoke the Lambda function on weekdays at 10:00 UTC. Feel free to change the cron to receive the notification whenever you want.

## 🙋 Heads Up  
Note that, when you send a SMS notification from your free trial project, it will begin with `Sent from a Twilio Trial account`. This message will be removed once your project has been upgraded. You can find more information about Twilio Free Trial limitations [here](https://help.twilio.com/articles/360036052753-Twilio-Free-Trial-Limitations#h_306ae9a5-c8bd-4859-9459-98acb7b4e3e3).

## 💻 Architecture Design
<img width="1255" height="737" alt="image" src="https://github.com/user-attachments/assets/c49e6b93-e72d-4f0e-b2a7-0aa2ed021136" />


