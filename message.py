from base import Bot


class Message:
    def __init__(self, bot: Bot):
        self.bot = bot

    def send_text(self, peer_id, msg):
        return self.bot.session.method("messages.send", {
            "peer_id": peer_id,
            "message": msg,
            "random_id": 0
        })

    def send_img(self, peer_id, photo):
        return self.bot.session.method("messages.send", {
            "peer_id": peer_id,
            "attachment": photo,
            "random_id": 0
        })

    def send_sticker(self, peer_id, sticker):
        return self.bot.session.method("messages.sendSticker", {
            "peer_id": peer_id,
            "random_id": 0,
            "sticker_id": sticker

        })

    def delete_message(self, id):
        str = self.bot.session.method("messages.delete", {
            "message_ids": f"{id}",
            "delete_for_all": 1

        })
        print(str)

    def get_members(self, peer_id):
        return self.bot.session.method("messages.getConversationMembers", {"peer_id": peer_id})
