# Description

This an web application based on the [Flask](https://flask.palletsprojects.com/) framework on the server side,
and the [Vue.js](https://vuejs.org/) javascript framework.
The front-end site of website is created using [Vuetify](https://vuetifyjs.com/)
and [Bootstrap 4.2](https://getbootstrap.com/docs/4.2/getting-started/introduction/)

## Table of contents
* [How it works ](#how-it-works)
* [Configuration](#configuration)
* [Dependencies](#dependencies)
* [Administration](#administration)
* [Database](#database)
* [Endpoints and blueprints](#endpoints-and-blueprints)
* [Usage](#usage)
* [Administrator account](#administrator-account)

# How it works

The server create routes and render templates for all of the pages in the website.
Server also create routes for the REST API which is used for receiving and transmitting data via HTTP protocol requests.
Then the data is dynamically fetched via Vue.js and displayed on the website.
There is socket connection created between the both sides.
This connection provide TCP communication for receiving messages and informing about changes in the users statuses.
The users and messages data is stored on MongoDb database on localhost.

# Configuration 

In config.py file it is possible to:
 - configure the secret key which flask app need to run.
 - configure the ip and port of the MongoDB.
  ```python
class Config:
    SECRET_KEY = "\xb6\x87\n\x10\x8cI0\xc1n\x0c\xf3s\x8f\xd8#\xa5X\x91:\xdd5\x80\xc6\xa6"
    MONGODB_SETTINGS = {"db": "ChatApp", "host": "mongodb://localhost:27017/ChatApp"}
```
 - configure the storage directory of the files sent by users.
  UPLOAD_FOLDER is a path to directory where the directories with the files sent via chat will be stored.
 - configure the allowed extensions of file that can be sent via chat.
```python
UPLOAD_FOLDER = r'C:\Users\kgolonka\Desktop\chat_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'}
```

# Dependencies

Python libraries needed for project to run can be found in the requirements.txt file.\
Application also need connection with MongoDB database.\
On the front-end side app use:
 - [Bootstrap 4.2](https://getbootstrap.com/docs/4.2/getting-started/introduction/), 
 - [jquery-3.3.1](https://jquery.com/), 
 - [VueJs](https://vuejs.org),
 - [Vuetify](https://vuetifyjs.com/)

# Administration

Pyhon file __init__.py in the app/CompanyApp directory starts the application on localhost.
To run the project you need to run this file. After running this file the flask framework starts on
the localhost:5000. 
Application can also be deployed outside localhost, but my solution doesn't provide this functionality.
Application on default is connected to the MongoDb on the localhost:27017 and it use ChatApp database.
The MongoDb database and connection can be configured.

# Database

Application uses MongoDB database running on the localhost:27017, host can be changed in config file.\
Database contains 4 collections:
##### assignments
Collection stores the registration documents created by users that filled register form.
##### chat_rooms
Collection stores the documents with information about the chat rooms. Each document contains unique chat room of two users.
The document is identified by the "participants" key which value is array of users in the room.
The value of "messages" key in each document contains all messages in chat room.
##### main_board
Collection stores the documents with messages in the 'Company chat' room.
##### users
Collection stores the document with information about registered users.

# Endpoints and blueprints.

Flask framework offer categorizing routes into the subgroups called blueprints.
```python
app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(main_board_bp, url_prefix="/board")
app.register_blueprint(authorization_bp, url_prefix="/authorization")
```
These blueprints are created in __init__.py. They provide the prefix to URL route.
Each blueprint have it's routes.

##### Main
/ - it is index page of app
##### Api
/api/users - REST API GET endpoint with users information\
/api/main_board - REST API  GET endpoint with main board messages\
/api/chat_rooms - REST API GET endpoint with chat rooms messages\
/api/main_board/send - REST API POST endpoint which post message\
/api/upload - REST API POST endpoint which post file
##### Authorization
/authorization/logout - it logout the user\
/authorization/ - it is login page\
/authorization/register - it is register page\
/authorization/assignments - it is administrator page for assignments
##### Main Board
/main_board/ - it is page of the chat application

# Usage
##### Registration

The /authorization/register route is made for registration.
User can go this page via the index page card 'New hire?'.
User need to fill the assignment and then it will be either approved or declined by administrator. 
##### Login

If the user have registered account it can logg in. The /authorization/ route is made for that purpose.
Link for that URL can be found in the index page or on the navbar.
User need to fill the login form with correct credentials to logg in.
##### Chat rooms

After logging in the user will be redirected to the chat page. 
On the left side user can find searchable list of available chats.
He can click at any chat and then the chat room will be set.
The first room is 'Company chat' which is room with all of the users.
The rest of the rooms are one on one room with another employee.
##### User status

After logging in the user status will be set to logged in.
The dot above the avatar of the another employee is employee's current status.
If the dot is grey that mean the employee is currently not logged in.
The green dot mean that employee is logged in.

##### Chatting

After setting the chat room, user can send the message by typing the message in the bar at the bottom of chat
and clicking either the blue arrow or enter key.
User can preview all the sent message by scrolling in the chat.

##### File transfer

At the bottom of the chat room there is a reddish button with clip icon. 
User can click that button to open 'Send file' card.
Then he can choose file and send it by clicking 'SEND' button

##### Logout

To logout user need to click Logout button in the right side of the navbar

# Administrator account

To approve or decline registration assignments administrator can either do it by operating in the database or via GUI.
Using GUI is possible after logging in as 'kamil'. The password is 'test'.
Then the /authorization/assignments route will be available.
Link to that URL will also be visible on the navbar.