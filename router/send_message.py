from fastapi import APIRouter
from pydantic import BaseModel
import jsonify

router = APIRouter()

# 接受者通用模型
class receiverType(BaseModel):
    isRoom: bool
    # atNameList: []
    name: str
    wxid: str
    # data: any


@router.post('/send_text')
async def send_text(data: receiverType):
    id: data.wxid
    name: data.name
    # atNameList = data.atNameList
    isRoom = data.isRoom
    # data: data.data

    # if data is None:
    #     raise HTTPException(status_code=400, detail="No data provided")
    
    # user = itchat.search_friends(name=name)

    # if user:
    #     itchat.send_msg(message, toUserName=user[0]['UserName'])
    #     return jsonify({"status": "success", "message": "Message sent!"}), 200
    # else:
    #     return jsonify({"status": "error", "message": "User not found!"}), 404