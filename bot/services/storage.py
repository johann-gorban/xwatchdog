from .config import CHAT_IDS_PATH
from typing import List

def get_chat_ids() -> List[int]:
    chat_ids = []
    with open(CHAT_IDS_PATH, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    chad_id = int(line)
                    chat_ids.append(chad_id)
                except ValueError:
                    pass
    return chat_ids


def add_chat_id(chat_id: int | str):
    if type(chat_id) == str:
        chat_id = int(chat_id)
    
    existing = get_chat_ids()

    if chat_id not in existing:
        with open(CHAT_IDS_PATH, 'a') as f:
            f.write(str(chat_id) + '\n')