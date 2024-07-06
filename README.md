# itchat-demo

基于 chatgpt-on-wechat 的itchat 写的demo，只实现了基本的登陆、自动回复、api推送，登陆、登出调用api, 基于微信网页版协仪-uos头

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

1. 只实现了一个推消息 API：http://localhost:5000/send_message

- method：post
- dataType: json
- 参数：{username: '昵称', message:'发送消息'}
期望可以帮我测试该版本多就掉线

2. 和该微信号聊天会回复你发送的文字

# Credit

[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)