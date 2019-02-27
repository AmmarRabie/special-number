from requests import put
from json import dumps, loads
from internet_status import internet
import data_handler as dh
config = loads(open("config.json").read())['test']

adminAuth = config["database secret"]
basePath = config["database base url"]


def setupToFirebase(posts):
    url = f"{basePath}/Z_definedMessages.json?auth={adminAuth}"
    res = put(url, data=dumps(posts))
    print("res for", url, "is", res)
    if(not res.ok):
        raise Exception("There is a problem, run the cmd again")
    # you can move posts files to exclude dir to reduce overhead of the network (fakes now)


if __name__ == '__main__':
    if(not internet()):
        raise Exception("No internet connection")
    postsIds = dh.getRegisteredPosts()
    posts = {}
    for postId in postsIds:
        info = dh.getPostData(postId)
        privateMessage = info['message']
        if(info['message'].strip() == ''):
            privateMessage = f"سعر الرقم \n {info['phone']} \n {info['price']} جنيه"
            # privateMessage = "سعر الرقم {} يساوي {}..".format(info['phone'], info['price'])
        privateMessage += "\n\n" + "لمزيد من الأرقام المميزة زور موقعنا" + "\n" + "https://nemrtyvip.com"
        posts[postId] = privateMessage
    setupToFirebase(posts)