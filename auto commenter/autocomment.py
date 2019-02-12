import requests
import json
from flask import Flask, request, make_response
from datetime import datetime
app = Flask(__name__)

VERIFY_TOKEN = 'testbotverifytoken'
#Insert facebook token here, this an non-expired token
PAGE_TOKEN = "EAAcpGsFBqk0BAAq2NStGNyU5BYXk5MprYZC4ZAlJKCG2CPxpm3TQ3xeKpBopKc92DDkc7m4Ywq0ouHLFzZBgfy1SHDxLEPZCa5fAMAILn81c1tFyEEoKhG3sFilgU6OlSXZCmXiyZA0KxIiMGzIcdPqmZCH53MOJDq7F4U7XcM4FQZDZD"

PAGE_ID = "1229774243814128" # chatbot tester

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    try:
        logFile = open('log.txt', 'a')
        body = request.get_json()
        print('\nthe whole body is\n', body, '\n\n')
        for change in body['entry'][0]['changes']:
            changeValue = change['value']
            # logFile.write(str(changeValue))
            logFile.write('\n\n')
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
            senderId = changeValue['from']['id']
            commentId = changeValue['comment_id']
            if (isRepeated(commentId)):
                print("NO: repeated callback")
                continue
            print('\n\nwe will reply to\n', changeValue, '\n\n')
            reply(senderId, commentId, 'This is the new auto comment reply')
        # posts = get_posts()
        # comment_on_posts(posts, 25)
    except Exception as e:
        print(e)
        # traceback.print_exc()
    finally:
        return make_response("Message Processed", 200)
        # return "Message Processed", 200
    return make_response("Message Processed", 200)


def reply(senderId, commentId, message):
    url = "https://graph.facebook.com/v3.2/{}/comments?access_token={}&message={}".format(commentId, PAGE_TOKEN, message)
    res = requests.post(url)
    print('reply with status code ', res.status_code)
    if(not res.ok):
        return
    # send him a message
    print('\nreplying....private message\n')
    url = "https://graph.facebook.com/v3.2/me/messages?access_token={}".format(PAGE_TOKEN)
    recipientId = senderId
    message = "this number costs a lot... it cost 3500"
    body = { "recipient": { "id": recipientId},"message": {"text": message}}
    res = requests.post(url, json=body)
    print('private message status', res.status_code)

def isRepeated(commentId):
    url = "https://graph.facebook.com/v3.2/{}/comments?access_token={}".format(commentId, PAGE_TOKEN)
    res = requests.get(url)
    print('res of getting comments=', res.status_code)
    if(not res.ok):
        return False
    commentsList = res.json()['data']
    print('\ncomments list is\n', commentsList)
    for comment in commentsList:
        if(comment['from']['id'] == PAGE_ID):
            return True
    return False

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid  token'
if __name__ == "__main__":
    app.run()
    # posts = get_posts()
    # comment_on_posts(posts, 25)


def replyPrivately(commentId, message):
    url = "https://graph.facebook.com/v3.2/{}/private_replies?message={}&access_token={}".format(commentId, message, PAGE_TOKEN)
    res = requests.post(url)
    print('replyPrivately status', res.status_code)
    if(not res.ok):
        print(res.json())
        return False, res.json()['error']['code']
    return True, 200

def comment_on_posts(posts, amount):
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/v3.2/{0}/comments".format(post['id'])
        message = "the time now is {}".format(datetime.now())
        parameters = {'access_token' : PAGE_TOKEN, 'message' : message}
        s = requests.post(url, data = parameters)
        print(s)
 
def get_posts():
    payload = {'access_token' : PAGE_TOKEN}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    result = json.loads(r.text)
    return result['data']