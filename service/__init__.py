import requests
from . import itchat
from . import wcf
from config import global_data
from common.dir import get_appdata_dir

wxBot = None

class WXBot:
    def __init__(self, logging):
        self.is_logged_in = False
        self.LOG = logging
        self.wxid = ''

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
    def sendTextMsg(self, wxid:str, name:str, msg: str, at_list: str= "") -> None:
    # def sendTextMsg(msg: str, wxid: str, at_list: str = "") -> None:
        """ 发送消息
        :param wxid: 接收人wxid或者群id
        :param name: 接受人昵称或者群昵称
        :param msg: 消息字符串
        :param at_list: 要@的wxid, @所有人的wxid为：notify@all
        """
        # msg 中需要有 @ 名单中一样数量的 @
        ats = ""
        if at_list:
            if at_list == "notify@all":  # @所有人
                ats = " @所有人"
            else:
                wxids = at_list.split(",")
                for id in wxids:
                    # 根据 wxid 查找群昵称
                    ats += f" @{self.provider.getAliasInChatroom(id, wxid)}"

        # {msg}{ats} 表示要发送的消息内容后面紧跟@，例如 北京天气情况为：xxx @张三
        if ats == "":
            self.LOG.info(f"To {wxid}: {msg}")
            self.provider.sendText(f"{msg}", wxid, at_list)
        else:
            self.LOG.info(f"To {wxid}: {ats}\r{msg}")
            self.provider.sendText(f"{ats}\n\n{msg}", wxid, at_list)
            
    # 获取所有联系人  格式: {"wxid": "NickName"}        
    def getAllContacts(self) -> dict:
        return self.provider.getAllContacts()

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
              self.LOG.info("Logged in successfully")
          except Exception as e:
              self.LOG.error(f"Error in login_callback: {e}")

        def logout_callback():
            try:
                requests.post(global_data['login_webhook'], json={'subject': 'itchat掉线', 'data':'logged_out'})
                self.LOG.info("Logged out successfully")
                self.is_logged_in = False
            except Exception as e:
                self.LOG.error(f"Error in logout_callback: {e}")

        self.provider.run(sessionDir=get_appdata_dir(), loginCallback=login_callback, exitCallback=logout_callback)

# 登陆方法
def runBot(logging):
    try:
       global wxBot
       wxBot = WXBot(logging)
       wxBot.run()
    except Exception as e:
        logging.error(f"Error in start_wxbot: {e}")


    
    