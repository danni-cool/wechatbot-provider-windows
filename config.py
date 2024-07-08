# 全局变量
global_data = {
  "provider": "web",
  "login_webhook": "https://example.com"
}

errorCode = {
  "GET_CONCAT_FAILED": {
    "errorCode": "-1000",
    "message": "获取联系人列表失败",
  },
  
  "MSG_SENT_FAILED": {
    "errorCode": "-2000",
    "message": "发送消息失败",
  }
}

def genErrorJsonRes(key:str):
  return errorCode[key]