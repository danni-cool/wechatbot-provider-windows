@echo off
setlocal

set VENV_DIR=.\venv
SET PATH=C:\Program Files\Python312;%PATH%     

if not exist "%VENV_DIR%" (
    echo Creating venv...
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate"
) else (
    echo venv already exists, skipping...
)

python -m pip install -r requirements.txt

endlocal