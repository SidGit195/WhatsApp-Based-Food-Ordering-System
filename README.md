# WhatsApp-Based Food Ordering System

A modern food ordering system that leverages WhatsApp integration for a seamless user experience. This project allows users to browse menus, place orders, and receive notifications through WhatsApp.

## 🎥 Demo Video
Click to watch the demonstration video of project: [https://www.youtube.com/watch?v=50BWrFlF5W8](https://www.youtube.com/watch?v=50BWrFlF5W8)

## Overview

This system consists of two main components:
- **Frontend**: Built with React 19 and modern JavaScript
- **Backend**: Python-based server with WhatsApp integration

## Features

- WhatsApp integration for order placement and notifications
- Intuitive menu browsing experience
- Real-time order tracking
- Secure payment processing
- Admin dashboard for restaurant owners

## Prerequisites

- Node.js v18+ for Frontend
- Python 3.8+ for Backend
- ngrok for WhatsApp webhook testing
- WhatsApp Twilio api

## Installation

### Frontend Setup

1. Navigate to the Frontend directory:
```bash
cd Frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

### Backend Setup

1. Navigate to the Backend directory:
```bash
cd Backend
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Start the server:
```bash
 uvicorn app.main:app
```

## WhatsApp Integration

1. Set up ngrok to expose your local server:
```bash
.\ngrok.exe config add-authtoken <paste-your-token-here>
```

```bash
.\ngrok.exe http 8000
```

2. Configure your WhatsApp Business API with the ngrok URL

3. Update the webhook URL in your backend configuration

## Configuration

Create a `.env` file in the Backend directory with the following variables:
```
DATABASE_URL=xxxxx
TWILIO_ACCOUNT_SID=xxxxx
TWILIO_AUTH_TOKEN=xxxxxx
TWILIO_WHATSAPP_FROM=xxxxxx
WHATSAPP_WEBHOOK_URL=xxxxx
STATUS_CALLBACK_URL=xxxxxx
```

## Screenshots
![whatsapp](https://github.com/user-attachments/assets/31e45116-f18c-4c91-b42f-106581a0d140)
![frontend](https://github.com/user-attachments/assets/365db560-c396-4e58-8ef3-e524e8685437)
![backend](https://github.com/user-attachments/assets/6a7cb0e9-94de-49b7-bb9c-5364a69a41b2)

