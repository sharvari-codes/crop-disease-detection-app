@echo off
REM Crop Disease Detection App - Launcher Script for Windows

echo.
echo ========================================
echo   Crop Disease Detection System
echo   Starting Application...
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Install/upgrade required packages if needed
echo.
echo Checking dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Launching Streamlit App...
echo ========================================
echo.
echo The app will open in your browser at:
echo   http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Streamlit app
streamlit run app.py

pause
