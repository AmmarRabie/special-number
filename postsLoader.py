from requests import put
from json import dumps, loads
from internet_status import internet
import data_handler as dh
config = loads(open("config.json").read())

adminAuth = config["database secret"]
basePath = config["database base url"]


def setupToFirebase(posts):
    url = "{}/Z_definedMessages.json?auth={}".format(basePath, adminAuth)
    res = put(url, data=dumps(posts))
    print("res for", url, "is", res)


if __name__ == '__main__':
    if(not internet()):
        raise Exception("No internet connection")
    postsIds = dh.getRegisteredPosts()
    posts = {}
    for postId in postsIds:
        info = dh.getPostData(postId)
        # comment = "تم الرد علي الخاص بالسعر"
        privateMessage = "سعر الرقم {} يساوي {}..".format(info['phone'], info['price'])
        posts[postId] = privateMessage
    setupToFirebase(posts)