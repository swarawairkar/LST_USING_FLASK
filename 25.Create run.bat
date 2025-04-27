@echo off
REM Script to run the Flask application on Windows

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in your PATH.
    exit /b 1
)

REM Check if the virtual environment exists
if exist venv (
    REM Activate the virtual environment
    call venv\Scripts\activate.bat
    echo Activated virtual environment.
) else (
    echo Warning: Virtual environment 'venv' not found.
    echo Consider creating a virtual environment with: python -m venv venv
)

REM Run the Flask application
echo Starting Flask application...
python run_flask_app.py

REM Deactivate virtual environment when script exits
if exist venv (
    call deactivate
)
