import requests
import data_handler as dh
from internet_status import internet
from json import loads

config = loads(open("config.json").read())['test']

PAGE_TOKEN = config["page access token"]
PAGE_ID = config["page id"]


COMMENT_ALREADY_REPLIED_CODE = 10900

def getObjectComments(objectId, limit=100):
    url = "https://graph.facebook.com/v3.2/{}/comments?order=reverse_chronological&limit={}&access_token={}".format(objectId, limit, PAGE_TOKEN)
    res = requests.get(url)
    if(not res.ok):
        print(res.json())
        raise Exception('not valid request', url)
    # TODO: Loop here in all paging then return the whole data
    return res.json()["data"]

def replyToNewPostComments(postId, privateMessage):
    # TODO: update to use paging, fetch 20 comments, if there is all not replied fetch the second 20 comments and so on till comments end or you get comment which is already replied
    postComments = getObjectComments(postId) # sorted by created time, and limit is infinite
    for comment in postComments:
        commentId = comment['id']
        success, errorCode = replyPrivately(commentId, privateMessage)
        if(not success and errorCode == COMMENT_ALREADY_REPLIED_CODE):
            continue
            # this assumption is not valid now after adding auto comment reply
            break # you don't need to loop over other older comments as this is already


def replyPrivately(commentId, message):
    url = "https://graph.facebook.com/v3.2/{}/private_replies?message={}&access_token={}".format(commentId, message, PAGE_TOKEN)
    res = requests.post(url)
    print('replyPrivately status', res.status_code)
    if(not res.ok):
        print(res.json())
        return False, res.json()['error']['code']
    return True, 200

if __name__ == '__main__':
    if(not internet()):
        raise Exception("No internet connection")
    postsIds = dh.getRegisteredPosts()
    for postId in postsIds:
        info = dh.getPostData(postId)
        privateMessage = info['message']
        if(info['message'].strip() == ''):
            privateMessage = f"سعر الرقم \n {info['phone']} \n {info['price']} جنيه"
        privateMessage += "\n\n" + "لمزيد من الأرقام المميزة زور موقعنا" + "\n" + "https://nemrtyvip.com"
        replyToNewPostComments(postId, privateMessage)