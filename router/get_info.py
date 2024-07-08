from fastapi import APIRouter
from model import commonResponse, create_success_response, create_error_response
from service import wxBot

router = APIRouter()

@router.get('/getAllContacts')
async def getAllContacts() -> commonResponse:
    try:
        result = wxBot.getAllContacts()
        return create_success_response(result)
    
    except Exception as e:
        return create_error_response("GET_CONCAT_FAILED")