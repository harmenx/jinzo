#!/bin/bash

# Uninstallation script for env-switcher

INSTALL_DIR="/usr/local/bin"
CONFIG_INSTALL_DIR="/usr/local/etc/env-switcher"
SCRIPT_NAME="env-switcher"

echo "Starting env-switcher uninstallation..."

# Remove the main script
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    sudo rm "$INSTALL_DIR/$SCRIPT_NAME"
    echo "Removed $INSTALL_DIR/$SCRIPT_NAME."
else
    echo "$INSTALL_DIR/$SCRIPT_NAME not found, skipping."
fi

# Remove the config directory
if [ -d "$CONFIG_INSTALL_DIR" ]; then
    sudo rm -R "$CONFIG_INSTALL_DIR"
    echo "Removed $CONFIG_INSTALL_DIR."
else
    echo "$CONFIG_INSTALL_DIR not found, skipping."
fi

# Optionally, uninstall Python dependencies. This is tricky as other projects might use them.
# For now, I'll just mention it.
echo "Note: Python dependencies (python-dotenv) were installed globally. You may want to uninstall them manually if no other projects use them: pip uninstall python-dotenv"

echo "Uninstallation complete."
