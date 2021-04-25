from flask_socketio import emit
from flask import request
from CompanyApp import socketio

USERS = {}


@socketio.on('add_user_socket')
def add_user_socket(username):
    if username:
        USERS[username] = request.sid
    emit('new_user_logged', broadcast=True)


@socketio.on('private_message')
def private_message(pay_load):
    user = USERS[pay_load['username']]
    if pay_load['friend'] in USERS.keys():
        friend = USERS[pay_load['friend']]
        emit('new_message', pay_load['username'], room=friend)
        emit('new_message', pay_load['friend'], room=user)
    else:
        if pay_load['friend'] == "general_chat":
            emit('new_message', pay_load['friend'], broadcast=True)
        else:
            emit('new_message', pay_load['friend'], room=user)
