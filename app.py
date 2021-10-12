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
    # message = TextSendMessage(text=event.message.text)
    # message = ImageSendMessage(
    #     original_content_url=".\\123.jpg",
    #     preview_image_url='\\123.jpg'
    # )
    message = VideoSendMessage(
        originalContentUrl='https://www.sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4',
        previewImageUrl='https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg'
    )
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
