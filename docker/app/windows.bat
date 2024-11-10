@echo off
setlocal

set VENV_DIR=.\venv
call "%VENV_DIR%\Scripts\activate"

echo Starting program...
python main.py

endlocal