
# itchat provider 适配 
import os
from lib import itchat
from lib.itchat.content import *

# 测试用api，需要删除
@itchat.msg_register(itchat.content.TEXT)
def demo_reply(msg):
  return 'Auto reply: ' + msg.text

# 发送文本消息
def sendText(wxid, name, msg, at_list):
  print('暂未实现')
  

# 根据 id 查找群昵称
def getAliasInChatroom(id=str, room_wxid=str):
  print('暂未实现')

# 获取所有联系人
def getAllContacts():
  print('暂未实现')

# 启动
def run(sessionDir, loginCallback, exitCallback):
  status_path = os.path.join(sessionDir, "../login-session-uos.pkl")
  itchat.auto_login(hotReload=True, enableCmdQR=2, statusStorageDir=status_path,loginCallback=loginCallback, exitCallback=exitCallback)
  itchat.run()

