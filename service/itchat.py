
# itchat provider适配 
import os
from lib import itchat
from lib.itchat.content import *

# 测试用api，需要删除
@itchat.msg_register(itchat.content.TEXT)
def demo_reply(msg):
  return 'Auto reply: ' + msg.text

# 启动
def run(sessionDir, loginCallback, exitCallback):
  status_path = os.path.join(sessionDir, "../session/itchat.pkl")
  itchat.auto_login(hotReload=True, enableCmdQR=2, statusStorageDir=status_path,loginCallback=loginCallback, exitCallback=exitCallback)
  itchat.run()

