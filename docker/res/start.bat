@echo off
setlocal

REM Step 1: Clone the repository if it does not exist
if not exist "wechatbotKit-py-http" (
    echo Cloning the repository...
    git clone https://github.com/danni-cool/wechatbotKit-py-http.git
) else (
    echo Repository already exists, skipping clone...
)

cd wechatbotKit-py-http

REM Default to pull the latest code
echo Pulling latest code from repository...
git pull

REM Step 2: Set up virtual environment
set VENV_DIR=.\venv

if not exist "%VENV_DIR%" (
    echo Creating venv...
    python -m venv "%VENV_DIR%"
    "%VENV_DIR%\Scripts\activate"
) else (
    echo venv already exists, skipping...
)

if exist requirements.txt (
    python -m pip install -r requirements.txt
) else (
    echo requirements.txt not found.
)

echo Starting program...
python main.py

endlocal