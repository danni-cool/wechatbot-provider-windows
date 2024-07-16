@echo off
setlocal

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