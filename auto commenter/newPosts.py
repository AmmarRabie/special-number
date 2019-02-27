from requests import get as rget
import data_handler as dh
from json import dumps as stringfy, loads
from internet_status import internet

config = loads(open("config.json").read())['test']

PAGE_TOKEN = config["page access token"]
PAGE_ID = config["page id"]


def getUnhandledPosts():
    url = "https://graph.facebook.com/v3.2/me?fields=feed{attachments{media}}&limit=7&order=reverse_chronological&access_token=" + PAGE_TOKEN
    res = rget(url)
    if(not res.ok):
        raise Exception('not valid request', url)
    allPosts = res.json()['feed']['data']
    newAddedPosts = []
    for post in allPosts:
        if(not post.get('attachments')):
            print("find post without image...ignoring")
            continue
        if(dh.isPostExcluded(post['id'])):
            # post is remarked excluded
            continue
        if(dh.isPostRegistered(post['id'])):
            # post is already registered, no need to move through all posts
            continue
        info = post['attachments']['data'][0]['media']['image']
        info.update({'id': post['id']})
        newAddedPosts.append(info)
        if (len(newAddedPosts) >= 5):
            break
    newPostsFile = open('new_posts.txt', 'w')
    newPostsFile.write(stringfy(newAddedPosts))

def main():
    if(not internet()):
        raise Exception("مفيييييش نت يا سيدناا")
    getUnhandledPosts()

if __name__ == '__main__':
    main()