# wechatbotKit-py-http

使用python3重新构建微信机器人api，底层对接 itchat 或者 wechatferry，作为容器统一对外的一部份

# Install

```bash
# 创建局部 python3 依赖环境
python3 -m venv ./venv

# 切换至当前依赖环境
source ./venv/bin/activate

# 安装依赖
python3 -m pip install -r requirements.txt

# 启动程序
python3 main.py
```

# Function

目前只实现了最简单的回复
1. 和该微信号聊天会回复你发送的文字

# Credit

- [chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)
- [WeChatFerry](https://github.com/lich0821/WeChatFerry)
