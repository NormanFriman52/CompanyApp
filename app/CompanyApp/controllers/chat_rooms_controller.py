from CompanyApp.database import db


def get_messages_with_id_lesser(messages, last_id):
    parsed_messages_list = []
    for message in messages:
        if message['msgId'] < last_id:
            parsed_messages_list.append(message)
    return parsed_messages_list


def get_room_messages(participants, limit=None, last_id=None):
    collection = db.get_collection("chat_rooms")
    room = collection.find_one({"participants": participants}, {"_id": 0, })
    messages = sorted(room['messages'], key=lambda k: k['msgId'], reverse=True)

    if last_id:
        messages = get_messages_with_id_lesser(messages, last_id)
        if limit:
            return messages[0:limit]
        return messages
    if limit:
        return messages[0:limit]
    return messages

