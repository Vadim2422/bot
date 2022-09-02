import os

from vk_api.bot_longpoll import VkBotEventType
from dotenv import load_dotenv
from Answers import Answer
from base import Bot
from message import Message
from server import keep_alive
load_dotenv()


bot = Bot(os.getenv('api_main'))
app = bot.longpool.listen()
mes = Message(bot)
keep_alive()
for event in app:
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            peer_id = event.object['message']['peer_id']
            if peer_id != 2000000004:
                break
            msg = event.object['message']['text'].lower()
            answer = Answer(mes, peer_id)
            if msg in ["кто на посту", "кто на посту?"]:
                answer.who_is_pidor()
            elif msg.startswith("в наряд "):
                answer.on_duty(msg)
            elif msg.startswith("в отставку "):
                answer.resignation(event.message['from_id'], msg)
            elif msg == '/help':
                answer.help()
