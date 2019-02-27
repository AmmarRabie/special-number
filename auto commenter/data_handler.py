from os import listdir
from os.path import isfile, join
from json import loads as jsonToDict
POSTS_PATH = "posts"
EXCLUDED_POSTS_PATH = "exclude"

def isPostExcluded(postId):
    return postId in getExcludedPosts()
def isPostRegistered(postId):
    return postId in getRegisteredPosts()
def getPostData(postId):
    postId = str(postId)
    f = open("{}/{}".format(POSTS_PATH, postId), encoding="utf-8")
    json = f.read()
    dataDict = jsonToDict(json)
    return dataDict


def getExcludedPosts():
    return [f for f in listdir(EXCLUDED_POSTS_PATH) if isfile(join(EXCLUDED_POSTS_PATH, f))]
def getRegisteredPosts():
    return [f for f in listdir(POSTS_PATH) if isfile(join(POSTS_PATH, f))]