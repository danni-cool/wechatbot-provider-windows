import logging
import ctypes
import os
import signal
import atexit
import time

global sdk
# 配置日志记录，将日志写入到 app.log 文件中
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
)


def cleanup():
    global sdk
    # 退出 SDK
    if sdk:
        if sdk.WxDestroySDK() != 0:
            logging.error("SDK 退出失败！")
    os._exit(-1)


def registerCleanup():
    atexit.register(cleanup)
    signal.signal(signal.SIGINT, cleanup)


def run():
    logging.info(f"SDK 初始化成功，rpc调用地址为：tcp://0.0.0.0:10086")
    try:
        while True:
            time.sleep(1)
    except Exception as e:
        logging.error("%s", e)
        cleanup()


def initialize_sdk():
    global sdk
    sdkPath = os.path.abspath(os.path.dirname(__file__))
    # 加载 sdk.dll （需要绝对路径）
    sdk = ctypes.cdll.LoadLibrary(f"{sdkPath}/sdk/sdk.dll")
    # 退出的时候停止消息接收，防止资源占用
    registerCleanup()
    # 初始化
    logging.info("SDK 初始化...")
    if sdk.WxInitSDK(True, 10086) != 0:
        logging.error("SDK 初始化失败！")
        os._exit(-1)


def main():
    while True:
        try:
            initialize_sdk()
            run()
        except Exception as e:
            logging.error("主循环异常: %s", e)
            time.sleep(5)  # 等待一段时间后重启


if __name__ == "__main__":
    main()
