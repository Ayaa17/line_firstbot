from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('9+lsi9ssuaA11KmxI4TBGHXopJkMFCZ+C53lm8BFou2yWrhhIOj8/B/tGLUgHoXIrBlZfIn86trOcpmR4Ac42Azwt/D569RCk8wbnIJMiQSqwZkPfDxT05JEnNu2VkZxMwXvKtDiPhQajE8rhyJt+AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f6ee193517c1148ceb905cfcb7b9afd5')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    print(event.message)
    line_bot_api.reply_message(event.reply_token, message)

# 貼圖訊息
@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = StickerSendMessage(
        package_id="446",
        sticker_id="1991"
    )
    line_bot_api.reply_message(event.reply_token, message)

#圖片訊息
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = ImageSendMessage(
        original_content_url="https://images.pexels.com/photos/4524371/pexels-photo-4524371.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        preview_image_url="https://images.pexels.com/photos/4524371/pexels-photo-4524371.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
    )
    line_bot_api.reply_message(event.reply_token, message)

#影片訊息
@handler.add(MessageEvent, message=VideoMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = VideoSendMessage(
        original_content_url ="https://vod-progressive.akamaized.net/exp=1634043402~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F780%2F22%2F553903899%2F2620242777.mp4~hmac=74dc296a0f11ecb7c619861289284e9488cba0d657842a7f603e8675e2b8a117/vimeo-prod-skyfire-std-us/01/780/22/553903899/2620242777.mp4?filename=pexels-shvets-production-8020523.mp4",
        preview_image_url ='https://images.pexels.com/videos/8020523/black-fashion-red-red-background-8020523.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
    )
    line_bot_api.reply_message(event.reply_token, message)

#音檔訊息
@handler.add(MessageEvent, message=AudioMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = AudioSendMessage(
        original_content_url='https://www.beatpick.com/storage/Mokhov/streaming/Mokhov_15847128.mp3',
        duration =240000,  #milliseconds
    )
    line_bot_api.reply_message(event.reply_token, message)

# 位置訊息
@handler.add(MessageEvent, message=LocationMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = LocationSendMessage(
        title="my location",
        address="1-6-1 Yotsuya, Shinjuku-ku, Tokyo, 160-0004, Japan",
        latitude="35.687574",
        longitude="139.72922"
    )
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    print(event.reply_token)
    print(event.message)
    message = ImagemapSendMessage(
        base_url='https://example.com/base',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='https://example.com/',
                area=ImagemapArea(
                    x=0, y=0, width=520, height=1040
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=0, width=520, height=1040
                )
            )
        ]
    )
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
