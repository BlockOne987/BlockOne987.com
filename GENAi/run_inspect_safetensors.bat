@echo off
REM Batch file to set up the environment and run the Python script

REM Step 1: Set the virtual environment directory
set VENV_DIR=venv

REM Step 2: Check if the virtual environment exists
if not exist %VENV_DIR% (
    echo Virtual environment not found. Creating one...
    python -m venv %VENV_DIR%
    if errorlevel 1 (
        echo Failed to create virtual environment. Exiting...
        exit /b 1
    )
    echo Virtual environment created.
)

REM Step 3: Activate the virtual environment
call %VENV_DIR%\\Scripts\\activate

REM Step 4: Install required dependencies
echo Installing dependencies...
pip install safetensors numpy torch
if errorlevel 1 (
    echo Failed to install dependencies. Exiting...
    exit /b 1
)

REM Step 5: Run the Python script
echo Running the Safe Tensor Inspector...
python inspect_safetensors.py
if errorlevel 1 (
    echo Script execution failed. Exiting...
    exit /b 1
)

REM Step 6: Deactivate the virtual environment
deactivate
echo Done.
pause
