@echo off

REM Ensure Python is available
if "%~1"=="" (
    echo Python executable path not provided. Exiting...
    exit /b 1
)

set "PYTHON_EXEC=%~1"

REM Ensure pip is installed
echo Checking if pip is installed...
"%PYTHON_EXEC%" -m ensurepip --default-pip
if %errorlevel% neq 0 (
    echo Failed to install pip. Exiting...
    exit /b 1
)

REM Upgrade pip to the latest version
echo Upgrading pip...
"%PYTHON_EXEC%" -m pip install --upgrade pip --user
if %errorlevel% neq 0 (
    echo Failed to upgrade pip. Exiting...
    exit /b 1
)

REM Install geocoder module
echo Installing geocoder module...
"%PYTHON_EXEC%" -m pip install geocoder --user
if %errorlevel% neq 0 (
    echo Failed to install geocoder. Exiting...
    exit /b 1
)

echo Dependencies installed successfully!
exit /b 0
