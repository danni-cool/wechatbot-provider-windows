import signal
import argparse
import logging
from config import global_data
from fastapi import FastAPI
from router import get_routers
from service import runBot, resetBot

# 配置日志记录，将日志写入到 app.log 文件中
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

def parse_args():
    parser = argparse.ArgumentParser(description="通过参数指定启动微信机器人协议，不同协议支持的api不同")
    parser.add_argument('--provider', type=str, default='web', help='默认 web 协议，也可使用 win 协议')
    return parser.parse_args()

def startFastApi():
    app = FastAPI()
    app.include_router(get_routers())
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

def main():
    args = parse_args()
    global_data['provider'] = args.provider
    logging.info(f"当前启动的是{global_data['provider']}协议")

    # 运行应用
    if __name__ == "__main__":
        runBot(logging)
        
        from threading import Thread
        Thread(target=startFastApi).start()
        
    signal.signal(signal.SIGINT, resetBot)

if __name__ == "__main__":
    main()