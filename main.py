import os
from lib import itchat
from lib.itchat.content import *
import requests
from flask import Flask, request, jsonify
import threading
import logging
from config import conf, get_appdata_dir

app = Flask(__name__)

WEBHOOK_URL = "http://your-webhook-url.com"  # 替换为你的 webhook URL
LOGIN_WEBHOOK = f"{WEBHOOK_URL}/login"
LOGOUT_WEBHOOK = f"{WEBHOOK_URL}/logout"

logging.basicConfig(level=logging.INFO)

# 登录成功时调用 webhook
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return 'Auto reply: ' + msg.text

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    username = data.get('username')
    message = data.get('message')
    
    user = itchat.search_friends(name=username)
    if user:
        itchat.send_msg(message, toUserName=user[0]['UserName'])
        return jsonify({"status": "success", "message": "Message sent!"}), 200
    else:
        return jsonify({"status": "error", "message": "User not found!"}), 404

def login_callback():
    try:
        requests.post(LOGIN_WEBHOOK, json={'status': 'logged_in'})
        logging.info("Logged in successfully")
    except Exception as e:
        logging.error(f"Error in login_callback: {e}")

def logout_callback():
    try:
        requests.post(LOGOUT_WEBHOOK, json={'status': 'logged_out'})
        logging.info("Logged out successfully")
    except Exception as e:
        logging.error(f"Error in logout_callback: {e}")

def start_itchat():
    try:
        status_path = os.path.join(get_appdata_dir(), "itchat.pkl")
        itchat.auto_login(hotReload=True, enableCmdQR=2, statusStorageDir=status_path,
                          loginCallback=login_callback, exitCallback=logout_callback)
        itchat.run()
    except Exception as e:
        logging.error(f"Error in start_itchat: {e}")

if __name__ == '__main__':
    from threading import Thread
    itchat_thread = Thread(target=start_itchat)
    itchat_thread.start()
    app.run(port=5000)
