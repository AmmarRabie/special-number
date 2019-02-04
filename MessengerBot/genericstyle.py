from flask import request

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
    },
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


class GenericReplyStyle():
    def __init__(self, bot, firebase):
        self.bot = bot
        self.db = firebase

    def handlePostRequest(self):
        print ("handle post request begins")

        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                print('all message is', message)
                self.handleOneMessage(message)
        return "Message Processed"
    
    def handleOneMessage(self, message):
        print("handle one message")
        Numbers=""
        result={} 
        if not message.get('postback'):
            return
        #Facebook Messenger ID for user so we know where to send response back to
        recipient_id = message['sender']['id']
        messagePayload = message["postback"]["payload"]
        if(messagePayload=="buy"):
            self.bot.send_generic_message(recipient_id,buttonTemplate)
            
        if messagePayload=="Vodafone_VIP":
            result= self.db.get('/T_Vodafone-vip',None)
        if messagePayload=="Vodafone_Special": 
            result= self.db.get('/T_Vodafone-special',None)
        if messagePayload=="Etisalat_VIP":
            result= self.db.get('/T_Etisalat-vip',None)
        if messagePayload=="Etisalat_Special":
            result= self.db.get('/T_Etisalat-special',None)
        if messagePayload=="Orange_VIP":
            result= self.db.get('/T_Orange-vip',None)
        if messagePayload=="Oragne_Special":
            result= self.db.get('/T_Orange-special',None)
        if messagePayload=="We_VIP":
            result= self.db.get('/T_We-vip',None)
        if messagePayload=="We_Special":
            result= self.db.get('/T_We-special',None)
        if result!={}:
            for key,value in result.items():
                if value=="Available":
                    Numbers=Numbers+key+"\n"
            self.send_message(recipient_id,Numbers)



    #uses PyMessenger to send response to user
    def send_message(self, recipient_id, response):
        #sends user the text message provided via input response parameter
        self.bot.send_text_message(recipient_id, response)
        return "success"
