import os

from files import read_json, write_json
from message import Message
from user import User


class Answer:

    def __init__(self, mes: Message, peer_id: int):
        self.mes = mes
        self.peer_id = peer_id
        self.user = User(mes.bot)

    def who_is_pidor(self):
        data = read_json(self.peer_id)
        if data and len(data['Pidory']):
            if len(data["Pidory"]) == 1:
                answer = "Пост пидора держит:\n"
            else:
                answer = "Пост пидора держат:\n"
            for line in data["Pidory"]:
                answer += "Пидор " + " @" + str(line) + '\n'
            self.mes.send_text(self.peer_id, answer)

        else:
            self.mes.send_text(self.peer_id, 'На посту никого')

    def on_duty(self, msg: str):
        if msg.find("club213701122") != -1:
            self.mes.send_img(self.peer_id, os.getenv('img_pnx'))
            return
        if not (msg.count('|') and msg.count('id') and msg.index('id') < msg.index('|')):
            self.mes.send_img(self.peer_id, os.getenv('img_incorrect'))
            return
        add_user = self.user.get_data(msg[msg.index("id"):(msg.index("|"))])
        print(add_user)
        members = self.mes.get_members(self.peer_id)
        check = False
        for member in members['items']:
            if member['member_id'] == add_user[0]['id']:
                check = True
                break
        if check:

            data = read_json(self.peer_id)
            user = self.user.get_id_or_domain(add_user)
            if data["Pidory"].count(user):
                self.mes.send_text(self.peer_id, "Пидор " + " @" + user + " уже на посту")
            else:
                data["Pidory"].append(user)
                write_json(data, self.peer_id)
                self.mes.send_text(self.peer_id, "Пост пидора принял @" + user)
        else:
            self.mes.send_img(self.peer_id, os.getenv('img_incorrect'))

    def resignation(self, from_id, msg):
        if not (msg.count('|') and msg.count('id') and msg.index('id') < msg.index('|')):
            self.mes.send_img(self.peer_id, os.getenv('img_incorrect'))
            return
        del_user = self.user.get_data(msg[msg.index("id"):(msg.index("|"))])
        data = read_json(self.peer_id)
        user = self.user.get_id_or_domain(del_user)
        if data["Pidory"].count(user):
            if del_user[0]['id'] != from_id:
                data["Pidory"].remove(user)
                write_json(data, self.peer_id)
                self.mes.send_text(
                    self.peer_id, f"Пост пидора сдал @{user}")
            else:
                self.mes.send_text(self.peer_id, f"Куда мы лезем? @{user}")
        else:
            self.mes.send_text(self.peer_id, "@" + user + " и так не пидор")

    def help(self):
        self.mes.send_text(self.peer_id, "1) Кто на посту\n2) В наряд @..\n3) В отставку @..")

