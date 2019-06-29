from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import app_setting

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        app_setting.handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@app_setting.handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    app_setting.line_bot_api.reply_message(event.reply_token,TextSendMessage(text))
    


if __name__ == "__main__":
    app.run()
