import requests
import data_handler as dh
VERIFY_TOKEN = 'testbotverifytoken'
# deek om token with auto comment token
PAGE_TOKEN = "EAAcpGsFBqk0BAFy0WZCMOv7DczpsRY0v8HByDRg8sh0t7qa7RvGO5PS2Ty9lZCn6iRKnt4f9UuYOvRyZCtFDw9q5KNCUaO8HlaDyJTAGlLgivbwGMnEdcIRAEfyKhu5PVUdZBeJWkcqgS9U8EATIGJMvTeA4iMXsEVPzp8MnoQZDZD"

# deek om token with another app
# PAGE_TOKEN = "EAADDhm1BDK0BACCapgrzH76ZC8ae0VvAYN4AONFTX4PGWNvicgBZBvSrBALtgU1aZACJb382mmgZAFkRWmkEkicFx3FJD5ZB0TQxaWOvM1LfYZB7nLl6sHs3BX249PObTy5fTZAYaQVBG5L2qohDIvVWl8T2UzEbY6yCUjQckTA4aESZCeHeWpLnAGrcXTDOol6UjOCZCJHnGdQZDZD"

# sherif token
# PAGE_TOKEN = "EAAFwsfhHYM0BALZBbyJuHwDm3vdZA0RiThI5ZAiZBlgbeg8eOMXmreQkujoKI6rLPd2q3UNrsVoY8Tq3c8qSUX3zfr7ns3ONQaBCKuZAGCtSbPOesR9DSRZCdp0NarVXQ0BaxLcOnCH0yq4aM2jQL3TzklpzYgKrDjslzfJVvRDgZDZD"
PAGE_ID = "330714580357868" # deek om elthanwya


def getObjectComments(objectId):
    url = "https://graph.facebook.com/v3.2/{}/comments?access_token={}".format(objectId, PAGE_TOKEN)
    res = requests.get(url)
    if(not res.ok):
        raise Exception('not valid request', url)
    # TODO: Loop here in all paging then return the whole data
    return res.json()['data']


def isPageReplied(replyes):
    for reply in replyes:
        if(reply['from']['id'] == PAGE_ID):
            return True
    return False
def replyToNewPostComments(postId, commentMessage, privateMessage):
    postComments = getObjectComments(postId)
    for comment in postComments:
        # print(comment)
        commentId = comment['id']
        replyes = getObjectComments(commentId)
        if(isPageReplied(replyes)):
            continue
        sendPrivateMessageTo("1952794271513237", privateMessage)
        if(comment.get('from')):
            print(comment['from']['name'])
            if(comment['from']['name'] == "Chatbot tester"):
                continue
            senderId = comment["from"]["id"]
            sendPrivateMessageTo("1952794271513237", privateMessage)
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

if __name__ == '__main__':
    postsIds = dh.getRegisteredPosts()
    for postId in postsIds:
        info = dh.getPostData(postId)
        comment = "تم الرد علي الخاص بالسعر"
        privateMessage = "سعر الرقم {} يساوي {}..".format(info['phone'], info['price'])
        replyToNewPostComments(postId, comment, privateMessage)