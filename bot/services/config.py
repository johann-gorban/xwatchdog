from pathlib import Path

ALERT_COOLDOWN_SEC = 600

CHAT_IDS_PATH = Path(__file__).resolve().parent.parent.parent / 'data' / 'chat_ids.txt'

CHAT_IDS_PATH.parent.mkdir(parents=True, exist_ok=True)

if not CHAT_IDS_PATH.exists():
    CHAT_IDS_PATH.touch()