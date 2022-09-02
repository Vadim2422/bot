import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


class Bot:

    def __init__(self, token):
        self.session = vk_api.VkApi(token=token)
        self.longpool = VkBotLongPoll(self.session, 213701122)
