import json
import os

path = 'conversations/'


def check_file(peer_id):
    if os.path.isfile(f"{path}{peer_id}.json"):
        return True
    else:
        return False


def read_json(peer_id):
    try:
        if not check_file(peer_id):
            file = open(f'{path}{peer_id}.json', 'w')
            print('{"Pidory": []}', file=file, end="")

        with open(f'{path}{peer_id}.json', 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, FileExistsError):
        print("error 1")
        return False


def write_json(data: dict, peer_id: int):
    try:
        with open(f"{path}{peer_id}.json", 'w') as file:
            json.dump(data, file, indent=3)
    except (FileNotFoundError, FileExistsError):
        print("error 2")


def write_file(path, data):
    try:
        with open(path, 'w') as f:
            print(*data, file=f, sep=", ")
    except (FileNotFoundError, FileExistsError):
        print("error 2")


def read_file(path):
    try:
        with open(path, 'r') as f:
            line = f.readline()
            return line
    except (FileNotFoundError, FileExistsError):
        print("error 2")



