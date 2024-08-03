# Weather Alert SMS Automation

This project fetches weather data from the OpenWeatherMap API and sends the weather details via SMS using the Twilio API. It demonstrates how to use Python for API integration and automation.

## Features

- Fetches current weather data based on geographic coordinates.
- Sends weather details via SMS using Twilio.

## Prerequisites

- Python 3.x
- Twilio account and phone number
- OpenWeatherMap API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SREERAJRAJEEV/Weather-Alert-via-SMS.git
   ```

2. Change into the project directory:

   ```bash
   cd Task-Reminder-Email-Automation
   ```

3. Install the required Python packages:

   ```bash
   pip install requests twilio
   ```

## Setup

1. Replace the placeholders in `main.py` with your actual credentials:

   ```python
   # OpenWeatherMap API key
   api_key = "your_openweathermap_api_key"

   # Twilio account SID and Auth Token
   account_sid = "your_twilio_account_sid"
   auth_token = "your_twilio_auth_token"

   # Twilio phone number and verified phone number
   from_="your_twilio_phone_number"
   to="your_verified_phone_number"
   ```

## Usage

Run the script to fetch weather data and send it via SMS:

```bash
python main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
