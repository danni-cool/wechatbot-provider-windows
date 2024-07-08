#!/bin/sh

# 定义虚拟环境目录
VENV_DIR="./venv"

# 检查虚拟环境是否存在
if [ ! -d "$VENV_DIR" ]; then
    echo "虚拟环境不存在，正在创建..."
    python3 -m venv $VENV_DIR
else
    echo "虚拟环境已存在，跳过创建步骤。"
fi

# 切换至当前依赖环境
echo "激活虚拟环境..."
source $VENV_DIR/bin/activate

# 检查requirements.txt文件是否存在
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt文件不存在，跳过安装步骤。"
else
    # 安装依赖
    echo "安装依赖..."
    python3 -m pip install -r requirements.txt
fi

# 启动程序
echo "启动程序..."
python3 main.py "$@"