# CompanyApp

This an web application based on the [Flask] (https://flask.palletsprojects.com/) framework on the server side,
and the [Vue.js] (https://vuejs.org/) javascript framework.
The front-end site of website is created using [Vuetify] (https://vuetifyjs.com/)
and [Bootstrap 4.2] (https://getbootstrap.com/docs/4.2/getting-started/introduction/)

# How it works?

The server create routes and render templates for all of the key pages in the website.
Also server create routes for the REST API which is used for receiving and transmitting data via HTTP protocol requests.
Then the data is dynamically fetched via Vue.js and displayed on the website.
There is socket connection created between the both sides.
This connection provide TCP communication for receiving messages and informing about changes in the users statuses.
The users and messages data is stored on MongoDb database on localhost.

#Configuration 

In config.py file it is possible to:
 - configure the secret key which flask app need to run.
 - configure the ip and port of the MongoDB.
  ```python
class Config:
    SECRET_KEY = "\xb6\x87\n\x10\x8cI0\xc1n\x0c\xf3s\x8f\xd8#\xa5X\x91:\xdd5\x80\xc6\xa6"
    MONGODB_SETTINGS = {"db": "ChatApp", "host": "mongodb://localhost:27017/ChatApp"}
```
 - configure the storage directory of the files sent by users.
 - configure the allowed extensions of file that can be sent via chat.
```python
UPLOAD_FOLDER = r'C:\Users\kgolonka\Desktop\chat_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'}
```
 
#Dependencies

Dependencies can be found in the requirements.txt file.

#Administration

Pyhon file __init__.py in the ../app/CompanyApp directory starts the application on localhost.
Application can also be deployed outside localhost, but my solution doesn't provide this functionality.

#Usage
##### Registration

The /authorization/register route is made for registration.
User can found href to the route on the index page on 'New hire?' card.
User need to fill the assignment and then it will be either approved or declined by administrator. 
##### Login

If the user have registered account it can logg in. The /authorization/ route is made for that purpose.
Href for that URL can be found in the index page or on the navbar.
User need to fill the login form with correct credentials to logg in.
##### Chat rooms

After logging in the user will be redirected to the chat page. 
On the left side user can find searchable list of available chats.
He can click at any chat and then the chat rooms will be set.
The first room is 'Company chat' which is room contacting all of the users.
The rest of the rooms are one on one room with another employee.
##### User status

After logging in the user status will be set to logged in.
The dot above the avatar of the another employee is employee's current status.
If the dot is grey that mean the employee is currently not logged in.
The green dot mean that employee is logged in.

##### Chatting

After setting the chat room ,user can send the message by typing the message in the bar at the bottom of chat
and clicking either the blue arrow or enter key.
User can preview all the sent message by scrolling in the chat.

##### File transfer

At the bottom of the chat room there is a reddish button with clip icon. 
User can click that button to open 'Send file' card.
Then he can choose file and send it by clicking 'SEND' button

##### Logout

To logout user need to click Logout button in the right side of the navbar

#Administrator account

To approve or decline registration assignments administrator can either do it by operating in the database or via GUI.
Using GUI is possible after logging in as 'kamil'. The password is 'test'.
Then the /authorization/assignments route will be available.
Href for that URL will also be visible on the navbar.