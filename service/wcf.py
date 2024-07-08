#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from wcferry import Wcf

wcf = None

# 发送文本消息
def sendText(msg, wxid, at_list):
  global wcf
  wcf.send_text(f"{msg}", wxid, at_list)

# 获取联系人（包括好友、公众号、服务号、群成员……）
def getAllContacts() -> dict:
  """
  获取联系人（包括好友、公众号、服务号、群成员……）
  格式: {"wxid": "NickName"}
  """
  global wcf
  contacts = wcf.query_sql("MicroMsg.db", "SELECT UserName, NickName FROM Contact;")
  return {contact["UserName"]: contact["NickName"] for contact in contacts}
    
# 根据 wxid 查找群昵称
def getAliasInChatroom(id=str, room_wxid=str):
  global wcf
  wcf.get_alias_in_chatroom(id, room_wxid)

# 启动wcf
def run(sessionDir, loginCallback, exitCallback):
    global wcf
    wcf = Wcf(debug=True)

def reset(sig, frame):
    global wcf
    wcf.cleanup()  # 退出前清理环境
    exit(0)
    
