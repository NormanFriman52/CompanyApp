from CompanyApp.database import db


def check_credentials(username, password):
    collection = db.get_collection("users")
    user = collection.find_one({"username": username, "password": password})
    if user:
        return user
    return {}
