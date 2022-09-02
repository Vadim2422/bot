from base import Bot


class User:

    def __init__(self, bot: Bot):
        self.bot = bot

    def get_data(self, id):
        account = self.bot.session.method("users.get", {"user_ids": id, "fields": "domain"})
        return account

    def get_id_or_domain(self, data):
        domain_id = data[0]['domain']
        if domain_id == "":
            return "id" + str(id)
        else:
            return domain_id
