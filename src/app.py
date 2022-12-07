import os
import sys

from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

# 新增
from src.machine import create_machine # import trick
from src.utils import send_text_message

load_dotenv()

# 新增
machines = {}

# 下面代碼完全來自 TOC2020

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", None)
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if CHANNEL_SECRET is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if CHANNEL_ACCESS_TOKEN is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(CHANNEL_SECRET)

"""
# 接收 LINE 的資訊
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
    return "OK"
"""

# 大坑，上面的 def callback(): 只是測試用的，實際上應該是下面這個 def webhook_handler():
# 才要加上 callback @app.route("/callback", methods=["POST"])
@app.route("/callback", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue

        # 修改
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()

        print(f"\nFSM STATE: {machines[event.source.user_id].state}")
        print(f"REQUEST BODY: \n{body}")

        # Advance the FSM for each MessageEvent
        response = machines[event.source.user_id].advance(event)

        # response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請依照指示與按鈕來操作!")

    return "OK"

"""
@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")
"""

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
