from requests import get as rget
import data_handler as dh
from json import dumps as stringfy
from internet_status import internet

# chatbot tester with auto comment token
PAGE_TOKEN = "EAAcpGsFBqk0BACGZAWHdnuMTPfzFY4UsKYSG3ObiZAAFfZBa1P3H23YSro9E1v3Ag2l2IKpSPx7o4o0wTh1gPZAnauqqUqEzh7MFfuZCMcJSTROHQG5jzDBB3FwkLUCDZBGwHIZBTStnhi1MPUgGwE0Ns56Kp4LaZBIR3RUMIiOe6wZDZD"
PAGE_ID = "1229774243814128" # chatbot tester


def getUnhandledPosts():
    url = "https://graph.facebook.com/v3.2/me?fields=feed{attachments{media}}&limit=20&order=reverse_chronological&access_token=" + PAGE_TOKEN
    res = rget(url)
    if(not res.ok):
        raise Exception('not valid request', url)
    # TODO: Loop here in all paging then return the whole data
    allPosts = res.json()['feed']['data']
    newAddedPosts = []
    for post in allPosts:
        if(not post.get('attachments')):
            # a post without an image is for sure not an Add post
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
        if (len(newAddedPosts) >= 20):
            break
    newPostsFile = open('new_posts.txt', 'w')
    newPostsFile.write(stringfy(newAddedPosts))

def main():
    if(not internet()):
        raise Exception("مفيييييش نت يا سيدناا")
    getUnhandledPosts()

if __name__ == '__main__':
    main()