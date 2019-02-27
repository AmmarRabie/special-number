# What is that
This is a fb bot which auto reply with a custom private reply to comments made by users on facebook page.
# Development
## overview
### fb access token ?
To use facebook graph api, you need a facebook app, any requests you make should be have an access token which assigned to an app.<br/>
Although app access token is restricted to do few things, so you need to upgrade -if we can say- it to include a user. with this token you can read email of the user and name by default and you can even request more permission scopes like reading his feed.<br/>
But our app need to deal with user pages. this type of requests have to be done within a page access token, so once again we need to upgrade our token from user access token to include a page of this user. At this point you can also request more powered permission scopes to do for this page.
![Access token example](https://github.com/AmmarRabie/special-number/blob/commenter/images/access_token.PNG?raw=true)
### App mode
The fb app can be in two states
- under development: where the app can gain all permission through [graph api explorer](https://developers.facebook.com/tools/explorer/), but not all users can interact with the app
- live: where some power permissions need to be gained through App Review process
### Webhooks
fb app can integrate for several products, one of them is the webhook.
You can say that Webhhok is a reversed api instead of hitting its endpoint, it hits your endpoint when an event occurs.
Facebook produce this solution for us, you provide them a url to be hit when a specific fb events occur.
**But your app should be live to listen to these changes**
## Our app case
Our app have to auto private reply to comments, so we need to configure a webhook with a live fb app. but also we need to reply to comments which require publish_pages permission which mean app review if app is live.
To go around that, we made **two fb apps**, one to handle webhook stuff in live mode, and other to handle private reply in development mode
## steps
1. make a live app, enter we will call it lapp (stands for live app), make a development app call it dapp
2. for lapp, integrate webhook with page subscription (enter url), then apply fields of feed
![integration of webhook](https://github.com/AmmarRabie/special-number/blob/commenter/images/webhook.PNG?raw=true)
3. Register your page for this app -> go to [graph api explorer](https://developers.facebook.com/tools/explorer/) and get an page access token of your page, then make a post request `{yourPageId}/subscribed_apps` like in this image
![post request](https://github.com/AmmarRabie/special-number/blob/commenter/images/registerPage.png?raw=true)
if success is true, you are done with this app
4. Now, select your dapp and get the page access token with publish_pages, manage_pages permissions.
5. open config.json file and put access token associated with dapp app and dapp app id
6. publish the code to google cloud functions and update the url instead of your pc computer in webhook lapp app
