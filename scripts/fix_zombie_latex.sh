#!/bin/bash

# Fix Zombie LaTeX Processes
# This script finds and kills any `latexmk` processes running on the system.

echo "Searching for stuck latexmk processes..."

# Find pids
PIDS=$(pgrep -f "latexmk")

if [ -z "$PIDS" ]; then
    echo "No latexmk processes found. Your system is clean!"
else
    echo "Found the following processes:"
    ps -fp $PIDS
    
    echo ""
    echo "Killing processes..."
    kill -9 $PIDS
    
    # Verify
    sleep 1
    CHECK=$(pgrep -f "latexmk")
    if [ -z "$CHECK" ]; then
        echo "Success! All processes terminated."
    else
        echo "Warning: Some processes might still be running."
    fi
fi
