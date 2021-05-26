"""
Module for configuration parameters.
"""


class Config():
    SECRET_KEY = "\xb6\x87\n\x10\x8cI0\xc1n\x0c\xf3s\x8f\xd8#\xa5X\x91:\xdd5\x80\xc6\xa6"
    MONGODB_SETTINGS = {"db": "ChatApp", "host": "mongodb://localhost:27017/ChatApp"}


UPLOAD_FOLDER = r'C:\Users\kgolonka\Desktop\chat_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'}