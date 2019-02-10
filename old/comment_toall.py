import requests
import data_handler as dh
VERIFY_TOKEN = 'testbotverifytoken'
# chatbot tester with auto comment token
PAGE_TOKEN = "EAAcpGsFBqk0BACGZAWHdnuMTPfzFY4UsKYSG3ObiZAAFfZBa1P3H23YSro9E1v3Ag2l2IKpSPx7o4o0wTh1gPZAnauqqUqEzh7MFfuZCMcJSTROHQG5jzDBB3FwkLUCDZBGwHIZBTStnhi1MPUgGwE0Ns56Kp4LaZBIR3RUMIiOe6wZDZD"

# deek om token with another app
# PAGE_TOKEN = "EAADDhm1BDK0BACCapgrzH76ZC8ae0VvAYN4AONFTX4PGWNvicgBZBvSrBALtgU1aZACJb382mmgZAFkRWmkEkicFx3FJD5ZB0TQxaWOvM1LfYZB7nLl6sHs3BX249PObTy5fTZAYaQVBG5L2qohDIvVWl8T2UzEbY6yCUjQckTA4aESZCeHeWpLnAGrcXTDOol6UjOCZCJHnGdQZDZD"

# sherif token
# PAGE_TOKEN = "EAAFwsfhHYM0BALZBbyJuHwDm3vdZA0RiThI5ZAiZBlgbeg8eOMXmreQkujoKI6rLPd2q3UNrsVoY8Tq3c8qSUX3zfr7ns3ONQaBCKuZAGCtSbPOesR9DSRZCdp0NarVXQ0BaxLcOnCH0yq4aM2jQL3TzklpzYgKrDjslzfJVvRDgZDZD"
# PAGE_TOKEN = "EAAFwsfhHYM0BALihDrQKUAM6ZCePlPPeuLd5eMzMSoIAW18DbKCdfTZAlgwwpXmRQnwegll5wEZBLXTU0rZACrfiZBlAD7mDZBbmTwGKSKPcxHrs8H1z9aDhj9cDWh18IGVZCiuchLfRvfA2vpg7VBHQTYZCawWffT7NvH9ZCeNIaKvvP6EWvsF15oSTB5EFwQXtBr3GnavfQmQZDZD"
PAGE_ID = "330714580357868" # deek om elthanwya
PAGE_ID = "1229774243814128" # chatbot tester


def getObjectComments(objectId):
    url = "https://graph.facebook.com/v3.2/{}/comments?access_token={}".format(objectId, PAGE_TOKEN)
    res = requests.get(url)
    if(not res.ok):
        print(res.json())
        raise Exception('not valid request', url)
    # TODO: Loop here in all paging then return the whole data
    return res.json()['data']


def isPageReplied(replyes):
    for reply in replyes:
        if(not reply.get('from')):
            continue
        if(reply['from']['id'] == PAGE_ID):
            return True
    return False
def replyToNewPostComments(postId, commentMessage, privateMessage):
    postComments = getObjectComments(postId)
    for comment in postComments:
        # print(comment)
        commentId = comment['id']
        replyes = getObjectComments(commentId)
        # sendPrivateMessageTo("2058754940874611", privateMessage) # ammar
        sendPrivateMessageTo("2064639840281784", privateMessage) # zozo
        if(isPageReplied(replyes)):
            continue
  
        # sendPrivateMessageTo("2058754940874611", privateMessage)
        return
        if(comment.get('from')):
            if(comment['from']['name'] == "زينب ربيع"):
                print(comment['from']['name'])
                print(comment['from']['id'])
                return
            print(comment['from']['name'])
            print(comment['from']['id'])
            continue
            senderId = comment["from"]["id"]
            sendPrivateMessageTo(senderId, privateMessage)
            # print(senderId)
            # commentOn(commentId, commentMessage)
        else:
            print("comment does not have from")
def commentOn(objetcId, message):
    url = "https://graph.facebook.com/v3.2/{}/comments?access_token={}&message={}".format(objetcId, PAGE_TOKEN, message)
    res = requests.post(url)
    print('comment on status code', res.status_code)
    if(not res.ok):
        print(url, res.json())
        raise Exception('invalid request with comment on' + ' status code ' + str(res.status_code))
    return True

def sendPrivateMessageTo(userId, message):
    url = "https://graph.facebook.com/v3.2/me/messages?access_token={}".format(PAGE_TOKEN)
    body = { "recipient": { "id": userId},"message": {"text": message}}
    res = requests.post(url, json=body)
    print('sendPrivateMessageTo status', res.status_code)
    if(not res.ok):
        print(res.json())
    else:
        raise Exception('message sent 5las')

if __name__ == '__main__':
    postsIds = dh.getRegisteredPosts()
    for postId in postsIds:
        info = dh.getPostData(postId)
        comment = "تم الرد علي الخاص بالسعر"
        privateMessage = "سعر الرقم {} يساوي {}..".format(info['phone'], info['price'])
        replyToNewPostComments(postId, comment, privateMessage)