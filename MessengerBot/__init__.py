from flask import Flask, request
from pymessenger.bot import Bot
import requests
from firebase import firebase
from genericstyle import GenericReplyStyle
from quickreply import QuickReplyStyle
app = Flask(__name__)
ACCESS_TOKEN = 'EAAcJ1mBp7YgBACFJrRzuOcJbolMBa7ZBIZCeMHOvXnFbQPoAFVFiCl5dZCDe2JkvQiHKdWjvDtCcNu1HbvBr3wg0DdOsH4DUafWKU5S39jCHDyTC5Mfya5J3ZBbOejvBqfNQZBP0uoJgQyXnlvN1S66fPeO1yZA1xQ0fsWrxhAQZBnkVzns8uIi'
VERIFY_TOKEN = 'testbotverifytoken'

bot = Bot(ACCESS_TOKEN)

firebase = firebase.FirebaseApplication('https://special-numbers.firebaseio.com/', None)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    try:
        style = QuickReplyStyle(bot, firebase)
        style.handlePostRequest()
    except:
        print("error")
    finally:
        return "Message Processed"
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid  token'

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()