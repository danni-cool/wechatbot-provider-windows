@echo off
setlocal

REM Step 2: Set up virtual environment
set VENV_DIR=.\venv

if not exist "%VENV_DIR%" (
    echo Creating venv...
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate"
) else (
    echo venv already exists, skipping...
)

python -m pip install -r requirements.txt

endlocal