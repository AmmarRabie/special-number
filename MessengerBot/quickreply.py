from flask import request

buttonTemplate=[
    {
        "content_type": "text",
        "title": "vodafone",
        "payload": "Vodafone",
        "image_url": "https://cdn2.iconfinder.com/data/icons/pack1-baco-flurry-icons-style/128/Vodafone.png",
    },
    {
        "content_type": "text",
        "title": "etisalat",
        "payload": "Etisalat",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Etisalat_Logo.svg/1200px-Etisalat_Logo.svg.png",
    },
    {
        "content_type": "text",
        "title": "orange",
        "payload": "Orange",
        "image_url": "https://specialnumber.net/storage/images/GF92Ntm84k2pBHZhQuUIyrMxZaubaf3kvdS9XtOx.png",      
    },
    {
        "content_type": "text",
        "title": "we",     
        "payload": "We",
        "image_url": "https://specialnumber.net/storage/images/qntzPAAFYs4zeTzuOoBpTTbxDiVfe7p2MaqFL3Mu.png",
    },
]

def specialtyType_quickReplyes(company):
    return [
        {
            "content_type": "text",
            "title":"VIP",
            "image_url":"https://cdn1.vectorstock.com/i/1000x1000/69/20/gold-vip-icon-vector-3876920.jpg",
            "payload":"{}_vip".format(company),
        },
        {
            "content_type": "text",
            "title":"Special",
            "image_url":"https://previews.123rf.com/images/ultrakreativ/ultrakreativ1205/ultrakreativ120500933/13802115-sign-symbol-stamp-or-icon-for-your-presentation-for-websites-and-many-more-named-special.jpg",
            "payload":"{}_special".format(company),
        }
    ]

class QuickReplyStyle():
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
        Numbers=""
        result={} 
        recipient_id = message['sender']['id']
        if message.get('postback'):
            #Facebook Messenger ID for user so we know where to send response back to
            messagePayload = message["postback"]["payload"]
            print(messagePayload)
            if(messagePayload=="buy"):
                # bot.send_generic_message(recipient_id,buttonTemplate)
                res = self.send_quick_replyes(recipient_id, quickReplyes=buttonTemplate, text='اختار الشركة')
                print(res)

        if message.get("message") and message.get("message").get("quick_reply"):
            print("quick_reply...")
            messagePayload = message["message"]["quick_reply"]["payload"]
            print(messagePayload)
            if(messagePayload in ["Vodafone", "Etisalat", "Orange", "We"]):
                res = self.send_quick_replyes(recipient_id, quickReplyes=specialtyType_quickReplyes(messagePayload), text='what category of number do you want')
                print(res)
            else:
                company, specialty = messagePayload.split('_')
                print(company, specialty)
                if(not (company and specialty)):
                    return "Message Processed"
                result = self.db.get('/T_{}-{}'.format(company, specialty), None)
                for key,value in result.items():
                    if value=="Available":
                        Numbers=Numbers+key+"\n"
                self.bot.send_text_message(recipient_id,Numbers)

    def send_quick_replyes(self, recipient_id, quickReplyes, text):
        payload = {
            'recipient': {
                'id': recipient_id
            },
            "message":{
                "text": text,
                "quick_replies": quickReplyes,
            }
        }
        return self.bot.send_raw(payload)