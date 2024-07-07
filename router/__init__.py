import os
import importlib
from fastapi import APIRouter

def get_routers():
    router = APIRouter()
    # 获取当前文件夹路径
    current_dir = os.path.dirname(__file__)
    # 遍历当前文件夹中的所有 Python 文件
    for file in os.listdir(current_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"router.{file[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "router"):
                router.include_router(module.router)
    return router
