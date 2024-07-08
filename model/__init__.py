from pydantic import BaseModel
from config import genErrorJsonRes
from typing import Any, Optional

class commonResponse(BaseModel):
  success: bool
  errorCode: int
  message: str
  data: Optional[Any]
  
def create_error_response(key: str, data: any) -> commonResponse:
    return commonResponse(
        success=False,
        **genErrorJsonRes(key),
        data=data
    )
    
def create_success_response(data = None) -> commonResponse:
  return commonResponse(
    success=False,
    errorCode=0,
    message="",
    data=data
  )