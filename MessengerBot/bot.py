#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import requests
from firebase import firebase

app = Flask(__name__)
ACCESS_TOKEN = 'EAAcJ1mBp7YgBADeSf9SvbZA6UDKDitZB6MbOkJHCMnZBFxOZCVXuGPZA8osIBFeX1XEaAfI0ZACVGXHTjAUOFiAsJZC5Nb8YZAshZA383dqQhTVgDW5LggBkLMaeDd1BE2GmtMqvE0PqHnPnLYPO7e6V8o5l8A9txVkk8o6oZBA0xsD7k1tIElnZADG'
VERIFY_TOKEN = 'loaiali'
bot = Bot(ACCESS_TOKEN)


buttonTemplate=[
 
 
    {
      "title":"Vodafone",
      
      "image_url":"https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Vodafone_2017_logo.svg/220px-Vodafone_2017_logo.svg.png",
      "buttons":
      [
        
        {
           "type":"postback",
           "payload":"Vodafone_VIP",
           "title":"VIP"

        },
        {
           "type":"postback",
           "payload":"Vodafone_Special",
           "title":"Special"
        }
      ]
    }
    ,
    {
      "title":"Etisalat",
     
      "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Etisalat_Logo.svg/1200px-Etisalat_Logo.svg.png",
      "buttons":
      [
        {
           "type":"postback",
           "payload":"Etisalat_VIP",
           "title":"VIP"

        },
        {
            
          "type":"postback",
          "payload":"Etisalat_Special",
          "title":"Special"

        }
      ]
    }
    ,
    {
      "title":"Orange",
      
      "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Orange_logo.svg/150px-Orange_logo.svg.png",
      "buttons":
      [
        {
           "type":"postback",
           "payload":"Orange_VIP",
           "title":"VIP"

        },
        {
        
          "type":"postback",
          "payload":"Oragne_Special",
          "title":"Special"
        
        }
      ]
    },
    {
      "title":"We",
      
      "image_url":"https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Telecom_Egypt_logo_AR.png/220px-Telecom_Egypt_logo_AR.png",
      "buttons":
      [
        {
           "type":"postback",
           "payload":"We_VIP",
           "title":"VIP"

        },
        {
              "type":"postback",
              "payload":"We_Special",
              "title":"Special"
        }
      ]
    },
]
  


firebase = firebase.FirebaseApplication('https://special-numbers.firebaseio.com/', None)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    Numbers=""
    result={} 
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
            
            

    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('postback'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                messagePayload = message["postback"]["payload"]
                if(messagePayload=="buy"):
                    bot.send_generic_message(recipient_id,buttonTemplate)
                    
                if messagePayload=="Vodafone_VIP":
                    result=firebase.get('/T_Vodafone-vip',None)
                if messagePayload=="Vodafone_Special": 
                    result=firebase.get('/T_Vodafone-special',None)
                if messagePayload=="Etisalat_VIP":
                    result=firebase.get('/T_Etisalat-vip',None)
                if messagePayload=="Etisalat_Special":
                    result=firebase.get('/T_Etisalat-special',None)
                if messagePayload=="Orange_VIP":
                    result=firebase.get('/T_Orange-vip',None)
                if messagePayload=="Oragne_Special":
                    result=firebase.get('/T_Orange-special',None)
                if messagePayload=="We_VIP":
                    result=firebase.get('/T_We-vip',None)
                if messagePayload=="We_Special":
                    result=firebase.get('/T_We-special',None)
                if result!={}:
                    for key,value in result.items():
                        if value=="Available":
                            Numbers=Numbers+key+"\n"
                    send_message(recipient_id,Numbers)
                       
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid  token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()