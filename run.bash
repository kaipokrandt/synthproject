#!/bin/bash
echo "I solemnly swear that I spent at least 4 solid hours working to build something in Python."
set -e

# Run the main.py script
echo "Running main.py..."
python3 main.py

# error checking
if python3 main.py; then
    echo "Script executed successfully!"
else
    echo "An error occurred while running main.py."
    exit 1
fi