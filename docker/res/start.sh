#!/bin/bash

# Step 1: Clone the repository if it does not exist
if [ ! -d "wechatbot-provider-windows" ]; then
    echo "Cloning the repository..."
    git clone https://github.com/danni-cool/wechatbot-provider-windows.git
else
    echo "Repository already exists, skipping clone..."
fi

cd wechatbot-provider-windows

# Default to pull the latest code
echo "Pulling latest code from repository..."
git pull

# Run wine windows.bat
echo "Running wine windows.bat..."
wine windows.bat