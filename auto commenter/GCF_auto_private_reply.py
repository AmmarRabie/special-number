'''
    This is for google cloud functions version
'''
from requests import post, get

VERIFY_TOKEN = 'testbotverifytoken'

# this token is useless => we need it for webhook
# app: auto comment reply ==> page: Auto comment reply ==> accound: عمار ربيع
PAGE_TOKEN = "EAAHRZAzYWZCrcBACD9pXIgVct6Fy0DePEbHQU32unNcW4OLCymbKvYrkcxzZCgOS85S6Aiv6mz09fEtRrstZBz2oFYI2KbSwqa0zLhTsdkh2rOmTwpXZCOgLXxOgZBR9TZB31IZCCcRLsy85929YwQIts8CWRISKUv8vwBLUiWeniAZDZD"


# app: auto comment ==> page: Auto comment reply ==> accound: عمار ربيع
PAGE_TOKEN = "EAAcpGsFBqk0BAEU1haVb89h1JYvQEt6RvK0An7qdF7BrJmgYkWJubWJU2eAA1UZBjZCp8nyckZAeK4NqV2Ed01g6FKWZBbas5yHhassE4fqIOVjQCevMZCx5P3wOq4RBK74eaSpFJkB9ZCywXq41ee5UagP9qGVvYSAEOtZC9FADtjyTTjZClGUd"
PAGE_ID = "622508538161975" # Auto comment reply


def root(request):
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        if(request.args and "hub.verify_token" in request.args):
            token_sent = request.args.get("hub.verify_token")
            return verify_fb_token(token_sent, request)
        return "Need token"
    try:
        body = request.get_json()
        for change in body['entry'][0]['changes']:
            changeValue = change['value']
            # don't handle our own actions
            if (changeValue['from']['id'] == PAGE_ID):
                print('NO: that is me :)')
                continue 
            # we will not handle anything except adding new comments
            if (changeValue['verb'] != 'add' or changeValue['item'] != 'comment'):
                print("NO: not new comment")
                continue
            # we will not handle replying of replying, means only reply one time when the comment parent is the post itself
            if (changeValue['post_id'] != changeValue['parent_id']):
                print("NO: not basic comment")
                continue
            # if code reach here, this is a new comment from real user adding a comment to a post in the page
            print("handle new comment")
            message, success = getMessageFromId(changeValue['post_id'])
            if(not success):
                print("this post is not registered yet, can't find id:", changeValue['post_id'])
                continue
            commentId = changeValue['comment_id']
            replyPrivately(commentId, message)
    except Exception as e:
        print(e)
        # traceback.print_exc()
    finally:
        return "Message Processed", 200
    return "Message Processed", 200


def getMessageFromId(postId):
    # message = get(f"https://special-number.firebaseio.com/Z_definedMessages/{postId}.json").text
    message = get(f"https://https://shaikh-sha3ban.firebaseio.com/Z_definedMessages/{postId}.json").text
    if (message == 'null'):
        return '', False
    return message, True
def verify_fb_token(token_sent, request):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid  token'


def replyPrivately(commentId, message):
    url = "https://graph.facebook.com/v3.2/{}/private_replies?message={}&access_token={}".format(commentId, message, PAGE_TOKEN)
    res = post(url)
    print('replyPrivately status', res.status_code)
    if(not res.ok):
        print(res.json())
        return False, res.json()['error']['code']
    return True, 200