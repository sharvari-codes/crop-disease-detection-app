#!/bin/bash
# Crop Disease Detection App - Launcher Script for Linux/Mac

echo ""
echo "========================================"
echo "  Crop Disease Detection System"
echo "  Starting Application..."
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Install/upgrade required packages
echo ""
echo "Checking dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements"
    exit 1
fi

echo ""
echo "========================================"
echo "  Launching Streamlit App..."
echo "========================================"
echo ""
echo "The app will open in your browser at:"
echo "  http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the Streamlit app
streamlit run app.py
