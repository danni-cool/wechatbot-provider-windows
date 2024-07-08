@echo off
setlocal

REM 定义虚拟环境目录
set VENV_DIR=.\venv

REM 检查python3是否存在
where /q python3
if errorlevel 1 (
    echo python3未找到，请确保它已经安装并添加到PATH中。
    exit /b
)

REM 检查虚拟环境是否存在
if not exist "%VENV_DIR%" (
    echo 虚拟环境不存在，正在创建...
    python3 -m venv %VENV_DIR%
) else (
    echo 虚拟环境已存在，跳过创建步骤。
)

REM 切换至当前依赖环境
echo 激活虚拟环境...
call %VENV_DIR%\Scripts\activate

REM 检查requirements.txt文件是否存在
if not exist "requirements.txt" (
    echo requirements.txt文件不存在，跳过安装步骤。
) else (
    REM 检查pip是否存在
    where /q pip
    if errorlevel 1 (
        echo pip未找到，请确保它已经安装并添加到PATH中。
        exit /b
    )
    REM 安装依赖
    echo 安装依赖...
    python -m pip install -r requirements.txt
)

REM 检查main.py文件是否存在
if not exist "main.py" (
    echo main.py文件不存在，无法启动程序。
    exit /b
)

REM 启动程序
echo 启动程序...
python main.py --provider win
