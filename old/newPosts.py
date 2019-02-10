import requests
import data_handler as dh
from json import dumps as stringfy
from internet_status import internet

# deek om token with auto comment token
PAGE_TOKEN = "EAAcpGsFBqk0BAMtgcg9JwT3jNgfoYCNz8FuZA4R4JsfHEaybqG7ghLGe03BePxzG01IskKI9Th5ZAdNTbZAnxQ19rfPh4vDanlCp5pE1iS1C59Wp5lmFOkgWxmNZBJHZAuwBQ6RfbA156puQ9kQwPidZAlaMfnhaZAdvbmKZAnlnrmNNcyAjcSG2"

# chatbot tester
PAGE_TOKEN = "EAAcpGsFBqk0BAIRYV5BF7dl5LC6ZAa1AVQCbvoYCZCPWoIrGezAyWimmlcXkND4ca3wlZAgET192vVXK1XQ93TpUhxnRLej0mtDJ5kfhym36y2UBbjK64SUSSl7qWNTPc9tZBMkc0m1KIypJZBrF0jZBv4yZCzq9QeG0DZCawZBio8hEd469iUSSDoQZBrdefU7iLDYQ3ZBDcimzgZDZD"


#PAGE_TOKEN = "EAAFwsfhHYM0BADRoLt0oznHeMwSXUMkYqqrX8umWQTOKkey3pTN4QvejZB7050iQyn2sBuwCZCGz6ygpmcWW8smVAdh2bNS6rLNxY5a1Mhv7qNzZCVZAxlDD72vA0h4ojAWQWdu6dttEAs6xWfRWk5bR9PuO7m1zREkftbusJsKrfcEkyedQ6QHCyf1LtXPxCzxlIlZCI3AZDZD"

def getUnhandledPosts():
    url = "https://graph.facebook.com/v3.2/me?fields=feed{attachments{media}}&access_token=" + PAGE_TOKEN
    res = requests.get(url)
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