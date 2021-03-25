from pymongo import MongoClient


MongoEngine = MongoClient()
db = MongoEngine.get_database("chat_app")
