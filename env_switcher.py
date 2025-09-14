import argparse
import os
import sys
from dotenv import load_dotenv

CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'config')
CURRENT_ENV_FILE = os.path.join(os.path.dirname(__file__), '.current_env')

def _get_available_environments():
    """Returns a list of available environments based on subdirectories in CONFIG_DIR."""
    if not os.path.exists(CONFIG_DIR):
        return []
    return [d for d in os.listdir(CONFIG_DIR) if os.path.isdir(os.path.join(CONFIG_DIR, d))]

def _set_current_environment(env_name):
    """Saves the current environment name to a file."""
    with open(CURRENT_ENV_FILE, 'w') as f:
        f.write(env_name)

def _get_current_environment():
    """Reads the current environment name from a file."""
    if os.path.exists(CURRENT_ENV_FILE):
        with open(CURRENT_ENV_FILE, 'r') as f:
            return f.read().strip()
    return "None"

def switch_environment(env_name):
    """Switches to the specified environment."""
    available_envs = _get_available_environments()
    if env_name not in available_envs:
        print(f"Error: Environment '{env_name}' not found. Available environments: {', '.join(available_envs)}")
        sys.exit(1)

    env_path = os.path.join(CONFIG_DIR, env_name)
    dotenv_path = os.path.join(env_path, '.env')
    docker_compose_path = os.path.join(env_path, 'docker-compose.yml')

    print(f"Switching to environment: {env_name}")

    # Load environment variables
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path, override=True)
        print(f"Loaded environment variables from {dotenv_path}")
    else:
        print(f"No .env file found for {env_name} at {dotenv_path}")

    # Start containers (if docker-compose.yml exists)
    if os.path.exists(docker_compose_path):
        print(f"Starting Docker containers for {env_name}...")
        # This command will be executed in the shell.
        # For a real tool, you might want to handle stdout/stderr more gracefully.
        os.system(f"docker-compose -f {docker_compose_path} up -d")
        print("Docker containers started.")
    else:
        print(f"No docker-compose.yml found for {env_name} at {docker_compose_path}")

    _set_current_environment(env_name)
    print(f"Successfully switched to {env_name} environment.")

def list_environments():
    """Lists all available environments."""
    available_envs = _get_available_environments()
    if not available_envs:
        print("No environments found in the 'config' directory.")
        return
    print("Available environments:")
    for env in available_envs:
        print(f"- {env}")

def show_status():
    """Shows the current active environment."""
    current_env = _get_current_environment()
    print(f"Current active environment: {current_env}")

def main():
    parser = argparse.ArgumentParser(description="CLI tool to switch between project environments.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Switch command
    switch_parser = subparsers.add_parser("switch", help="Switch to a specified environment.")
    switch_parser.add_argument("environment", type=str, help="The name of the environment to switch to (e.g., dev, staging, production).")

    # List command
    list_parser = subparsers.add_parser("list", help="List all available environments.")

    # Status command
    status_parser = subparsers.add_parser("status", help="Show the current active environment.")

    args = parser.parse_args()

    if args.command == "switch":
        switch_environment(args.environment)
    elif args.command == "list":
        list_environments()
    elif args.command == "status":
        show_status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
