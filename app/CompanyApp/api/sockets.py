"""
This module create the sockets for client server communication.
"""
from flask_socketio import emit
from flask import request
from CompanyApp import socketio

USERS = {}


@socketio.on('add_user_socket')
def add_user_socket(username):
    """
    Create add_user socket. Function add the username to USERS dict as a key and sid as value.
    Emit the broadcast message that new user logged in.
    :param username: name of the user
    :return: None
    """
    if username:
        USERS[username] = request.sid
    emit('new_user_logged', broadcast=True)


@socketio.on('private_message')
def private_message(pay_load):
    """
    Create private_message socket.
    Function check if the user is logged and then emit the massage to friend and user that new message was sent.
    If the payload 'friend' key is 'general_chat' it emit broadcast message that new message was sent to logged users.
    :param pay_load: dictionary with 'username' and 'friend' keys
    :return: None
    """
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
