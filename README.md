![Python](https://img.shields.io/badge/python-3.11-blue)
![Terraform](https://img.shields.io/badge/terraform-1.12.2-623ce4)
![Gemini](https://img.shields.io/badge/gemini%20flash-2.0-ff69b4)

# TinyKraken 🐙
TinyKraken is a lightweight personal tool that sends SMS reminders to help you stay hydrated throughout the day. If you're the kind of person who forgets to drink water (like me), TinyKraken has your back — one message at a time.

## 🧠 What Does It Do?
TinyKraken sends a simple SMS message to your phone reminding you to drink water every weekday at 10:00 UTC. Messages are generated using **Gemini AI** to make them less repetitive or more encouraging. Messages are stored to DynamoDB for tracking purposes.

## 📦 Pre-requisites

- Have **Python** installed, specifically `3.11`. 
- A **Twilio account** (to buy a phone number and send SMS notifications). 
- A **Gemini AI API key** (for message generation).
- An **AWS Account** to create the following resources:
   - An `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to allow Terraform creates the infrastructure.
   - A S3 bucket called `tiny-kraken`. This is required as `.tfstate` is stored there.
- **Terraform**.
   - Follow this [documentation](https://developer.hashicorp.com/terraform/install) to install Terraform based on your OS.
  
## ☁️ API Setup

### Python 🐍
1. Simply download the installer from the [official Python website](https://www.python.org/).
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
2. Simply follow this [documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) to create a S3 bucket.

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
 - Initializes Terraform and creates the infrastructure to AWS.

## 🔥 How To Use It
Right now, AWS EventBridge Scheduler is scheduled to invoke the Lambda function on weekdays at 10:00 UTC. Feel free to change the cron (either directly in the code or once the EventBridge Scheduler is created) to receive the notification whenever you want.

## 🙋 Heads Up  
Note that, when you send a SMS notification from your Twilio free trial project, the message will begin with `Sent from a Twilio Trial account`. This will be removed once you upgrade your Twilio project. You can find more information about Twilio Free Trial limitations [here](https://help.twilio.com/articles/360036052753-Twilio-Free-Trial-Limitations#h_306ae9a5-c8bd-4859-9459-98acb7b4e3e3).

## 👮 Authentication
To access the API Gateway resources, you must authenticate using valid AWS credentials. Specifically, an `Access Key ID`, `Secret Access Key` and `Region` are required. 

You can generate these credentials by following this [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys-admin-managed.html#admin-create-access-key) or simply use the credentials you created during the [API Setup](https://github.com/apaytuvigallart/TinyKraken?tab=readme-ov-file#%EF%B8%8F-api-setup). Resources are created in `eu-west-1`, so you must specify that region.

Once generated, provide these credentials in your requests to ensure secure access to the API Gateway. For reference, you can review this example using [Postman](https://www.postman.com/). 

<img width="1143" height="603" alt="image" src="https://github.com/user-attachments/assets/f267a4a4-18e6-43a0-a308-076281000b16" />

## 💻 Architecture Design
### hydration_reminder
<img width="1797" height="827" alt="image" src="https://github.com/user-attachments/assets/8221dd3c-cf18-4877-98b2-6aa35e037217" />

### api
<img width="983" height="445" alt="image" src="https://github.com/user-attachments/assets/2243f249-5988-400f-a878-142b6fc6594f" />
