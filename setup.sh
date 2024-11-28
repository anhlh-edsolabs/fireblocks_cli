#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if command_exists python3; then
    echo "Python is already installed."
else
    echo "Python is not installed. Installing Python..."
    # Install Python based on the OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-venv python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Check if Homebrew is installed
        if ! command_exists brew; then
            echo "Homebrew is not installed. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew upgrade
        brew install python
    else
        echo "Unsupported OS. Please install Python manually."
        exit 1
    fi
fi

# Check if pip is installed
if command_exists pip3; then
    echo "pip is already installed."
else
    echo "pip is not installed. Installing pip..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get install -y python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install pip
    else
        echo "Unsupported OS. Please install pip manually."
        exit 1
    fi
fi

# Create and activate a virtual environment
echo "Creating and activating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install fireblocks-sdk

# Instructions for adding API key and secret
echo "Setup complete. Please add your Fireblocks API key and secret:"
echo "1. Place your API key in 'src/api_key.txt'."
echo "2. Place your API secret in 'src/quantum_main.key'."

# Deactivate the virtual environment
deactivate

echo "Setup finished. You can now run the script using 'python src/fireblocks_cli.py' or 'python3 src/fireblocks_cli.py'."
