# Telegram Air Quality Sensor Bot

Reusable Python template for a Telegram chatbot that queries environmental sensor data from an HTTP API, generates time-series plots, exports CSV files, and classifies air quality using configurable thresholds.

This repository is intended for educational and research projects. It does not include private API tokens, Telegram tokens, SSH keys, server IPs, or deployment-specific secrets.

## Features

- Telegram interface using buttons.
- Multi-device configuration.
- Sensor selection.
- Latest sensor reading.
- Normative rolling averages:
  - PM2.5 and PM10: 12-hour average.
  - NO2: 1-hour average.
- Configurable air-quality classification bands.
- Time-series plots with minimum, maximum, and average values.
- CSV export for multiple sensors.
- Configuration via YAML and `.env`.

## Supported sensor types

The example configuration includes:

- PM2.5
- PM10
- NO2
- Relative Humidity
- Temperature
- Location

## Project structure

```text
.
├── cfg/
│   ├── devices.example.yaml
│   ├── norms.yaml
│   └── sensors.yaml
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── cfg.py
│   ├── csvx.py
│   ├── dev.py
│   ├── dt.py
│   ├── menus.py
│   ├── norm.py
│   ├── plot.py
│   ├── state.py
│   └── tg_bot.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Security notes

Never commit or publish:

- `.env`
- Telegram bot tokens
- API tokens
- SSH private keys such as `.pem` files
- CSV exports with real data
- Server IP addresses
- Private deployment instructions

Use `.env.example` as a template and create your own private `.env` file locally.

## Local setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Create your local environment file:

```bash
cp .env.example .env
```

Edit `.env` with your own Telegram token and API tokens.

Create your local device configuration:

```bash
cp cfg/devices.example.yaml cfg/devices.yaml
```

Edit `cfg/devices.yaml` with your own device names and environment variable names.

## Required environment variables

Example `.env`:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
SMABILITY_BASE_URL=https://example.com/SmabilityAPI
SM_TOKEN_DEVICE_1=your_device_1_api_token_here
SM_TOKEN_DEVICE_2=your_device_2_api_token_here
TZ=America/Mexico_City
```

The variable names in `cfg/devices.yaml` must match the token variable names in `.env`.

Example:

```yaml
devices:
  device_1:
    label: "Equipo 1"
    env_token: "SM_TOKEN_DEVICE_1"

  device_2:
    label: "Equipo 2"
    env_token: "SM_TOKEN_DEVICE_2"
```

## Running locally

```bash
python src/tg_bot.py
```

The bot uses polling, so no public webhook URL is required for local testing.

## Configuration files

### `cfg/devices.yaml`

Local-only file that maps devices to environment variables containing API tokens.

Do not commit the real `cfg/devices.yaml` if it contains private deployment details.

### `cfg/devices.example.yaml`

Safe example version intended for GitHub.

### `cfg/sensors.yaml`

Defines sensor IDs, aliases, display labels, and units.

### `cfg/norms.yaml`

Defines air-quality classification bands.

## Production deployment

This template can be deployed to a Linux server or cloud VM such as AWS EC2.

Recommended production approach:

- Use a Python virtual environment.
- Store `.env` only on the server.
- Run the bot with `systemd`.
- Review logs with `journalctl`.
- Keep SSH keys and tokens outside the repository.

Do not publish real server IPs, SSH key names, or production tokens in this repository.

## Development notes

Recommended files to ignore:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
.DS_Store
*.pem
*.key
*.csv
*.log
cfg/devices.yaml
README.private.md
src/test_*.py
```

## License

Add a license before publishing if you want others to reuse or modify this project.
