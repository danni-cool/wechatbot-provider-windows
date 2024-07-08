from fastapi import APIRouter
from pydantic import BaseModel
from service import wxBot
from model import create_success_response, create_error_response
from typing import Any, Optional

router = APIRouter()
# 接受者通用模型
class receiverType(BaseModel):
    wxid: str
    name: str
    atList: list[str]
    message: Optional[Any]

@router.post('/sendMsg')
async def send_text(data: receiverType):
    id: data.wxid
    name: data.name
    msg: data.message
    atList = data.atList
    
    try:
        wxBot.sendTextMsg(id, name, msg, atList)
        return create_success_response("消息发送成功")
    
    except Exception as e:
        return create_error_response("MSG_SENT_FAILED")