#!/bin/bash

# Installation script for env-switcher

INSTALL_DIR="/usr/local/bin"
CONFIG_INSTALL_DIR="/usr/local/etc/env-switcher"
SCRIPT_NAME="env-switcher"
PYTHON_SCRIPT="env_switcher.py"
REQUIREMENTS_FILE="requirements.txt"

echo "Starting env-switcher installation..."

# Create installation directories if they don't exist
sudo mkdir -p "$INSTALL_DIR"
sudo mkdir -p "$CONFIG_INSTALL_DIR"

# Copy the main script
sudo cp "$PYTHON_SCRIPT" "$INSTALL_DIR/$SCRIPT_NAME"
sudo chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
echo "Copied $PYTHON_SCRIPT to $INSTALL_DIR/$SCRIPT_NAME and made it executable."

# Copy the config directory
sudo cp -R config "$CONFIG_INSTALL_DIR/"
echo "Copied config directory to $CONFIG_INSTALL_DIR/"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r "$REQUIREMENTS_FILE"

echo "Installation complete! You can now run 'env-switcher <command>' from anywhere."
echo "Example: env-switcher list"
