import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "0")) # Defaulting to "0" as int for safety if not set
API_HASH = os.environ.get("API_HASH", "")
ADMINS = int(os.environ.get("ADMINS", "0")) # Defaulting to "0" as int for safety
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "") # Will be an empty string if not set
