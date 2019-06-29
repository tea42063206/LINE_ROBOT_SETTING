from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Channel access token')
handler = WebhookHandler('Channel secret')
