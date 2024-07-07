import requests
from . import itchat
from . import wcf
from config import global_data
from common.dir import get_appdata_dir

class WXBot:
    def __init__(self, logging):
        self.is_logged_in = False
        self.logging = logging

        provider = {
            'web': itchat,
            'win': wcf
        }

        provider_key = global_data['provider']
        self.provider = provider[provider_key]

    # 搜索好友
    def search_friends(wxid, name):
      print()

    # 发送文本
    def send_text():
      print()

    # 发送图像
    def send_pic():
      print()
    
    # 发送文件
    def send_file():
       print()
  
    # 等待添加

    # 启动微信机器人    
    def run(self):
        """
        运行微信机器人
        """
        def login_callback():
          try:
              requests.post(global_data['login_webhook'], json={'subject': 'itchat登陆', 'data':'logged_in'})
              self.is_logged_in = True
              self.logging.info("Logged in successfully")
          except Exception as e:
              self.logging.error(f"Error in login_callback: {e}")

        def logout_callback():
            try:
                requests.post(global_data['login_webhook'], json={'subject': 'itchat掉线', 'data':'logged_out'})
                self.logging.info("Logged out successfully")
                self.is_logged_in = False
            except Exception as e:
                self.logging.error(f"Error in logout_callback: {e}")

        self.provider.run(sessionDir=get_appdata_dir(), loginCallback=login_callback, exitCallback=logout_callback)

# 登陆方法
def start(logging):
    try:
       bot = WXBot(logging)
       bot.run()
    except Exception as e:
        logging.error(f"Error in start_wxbot: {e}")


    
    