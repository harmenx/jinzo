# Env Switcher

A command-line tool to quickly switch between different project environments (development, staging, production). It loads environment variables from `.env` files and starts/stops Docker containers using `docker-compose.yml` files for each environment.

## Features

- Switch between predefined environments
- Load environment-specific variables
- Automatically start Docker containers for the selected environment
- List available environments
- Show current active environment

## Requirements

- Python 3.6+
- Docker and Docker Compose
- `python-dotenv` library (version 1.0.0)

## Installation

1. Clone or download this repository.

2. Install the required Python package:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Docker and Docker Compose are installed and running on your system.

## Configuration

Create a `config/` directory in the project root. For each environment, create a subdirectory (e.g., `dev/`, `staging/`, `production/`) containing:

- `.env`: Environment variables for the environment
- `docker-compose.yml`: Docker Compose configuration for the environment

Example structure:
```
config/
├── dev/
│   ├── .env
│   └── docker-compose.yml
├── staging/
│   ├── .env
│   └── docker-compose.yml
└── production/
    ├── .env
    └── docker-compose.yml
```

### Example .env file
```
ENV_NAME=development
DATABASE_URL=postgresql://user:password@localhost:5432/dev_db
API_KEY=dev_api_key
```

### Example docker-compose.yml
```yaml
version: '3.8'
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: dev_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
```

## Usage

Run the script from the project root directory.

### Switch to an environment
```
python env_switcher.py switch <environment_name>
```
Example:
```
python env_switcher.py switch dev
```

This will:
- Load environment variables from `config/dev/.env`
- Start Docker containers defined in `config/dev/docker-compose.yml`

### List available environments
```
python env_switcher.py list
```

### Show current active environment
```
python env_switcher.py status
```

## Commands

- `switch <env>`: Switch to the specified environment
- `list`: List all available environments
- `status`: Show the current active environment

## Notes

- The tool saves the current environment in a `.current_env` file in the project root.
- If no `.env` or `docker-compose.yml` file exists for an environment, the tool will notify you but continue.
- Ensure Docker is running before switching environments that use Docker Compose.

## Contributing

Feel free to submit issues or pull requests.

## License

This project is open-source. See LICENSE file for details (if applicable).
