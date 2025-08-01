# TinyKraken 🐙
TinyKraken is a lightweight personal tool that sends SMS reminders to help you stay hydrated throughout the day. If you're the kind of person who forgets to drink water (like me), TinyKraken has your back — one message at a time.

## 🧠 What Does It Do?
TinyKraken sends a simple SMS message to your phone reminding you to drink water. Messages can be generated or personalized using **Gemini AI** to make them less repetitive or more encouraging.

> 🔔 **Note:** TinyKraken currently relies on a **manual scheduler**, such as a **cron job** on your system. In future versions, AWS-based automation (Lambda, EventBridge) will be available.

## 📦 Requirements

- The dependencies listed in `requirements.txt` (installed via `install.sh`).
- A **Twilio account** (to buy a phone number and send SMS).
- A **Gemini AI API key** (for message generation).

## ☁️ API Setup

### 🔹 Twilio (for sending SMS)

1. **Create a Twilio Account**: [https://www.twilio.com/](https://www.twilio.com/).
2. **Free Trial**: New accounts receive **$15 in credits**, enough for basic usage.
3. **Buy a Phone Number**: Required to send messages.
4. **Grab Your Credentials**:
   - Account SID.
   - Auth Token.
   - Twilio Phone Number.
   - Your Phone Number.

### 🔹 Gemini AI (for generating/personalizing messages)

1. Simply follow [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key) to create a key for free.

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
This script:
- Creates and activates `.venv` if it doesn't exist.
- Creates `.env`, if it doesn't exist.
- Installs dependencies from `requirements.txt`.
- Asks to set up the Environment Variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`
   - `TO_PHONE`
   - `GEMINI_API_KEY`

## 🔥 How To Use It
Simply activate the virtual environment and run `main.py`.
```bash
source .venv/bin/activate
python hydration_reminder/main.py
```

## ⏱️ How to Schedule It

TinyKraken does not currently handle scheduling on its own. You need to use a system scheduler like cron (Linux/macOS) or Task Scheduler (Windows).

## 🛠️ Coming Soon
TinyKraken will soon support cloud-based automation using:
- AWS Lambda (to run the Python script)
- Amazon EventBridge (to schedule reminders)
- Terraform (to manage infrastructure)

This will eliminate the need for local scheduling and make deployment easier.
