'''
    To make an auto private comment reply, we need two facebook apps
    one for "auto" and second is for "comment reply"
    to make an auto respond this means "webhook" => and to enable webhook for interactions you must have an "live app"
    to make a private reply you have to have an access token with publish_pages permission, to get this you make your app in development mode or go through app review
    so we have an app with webhook in live mode, and have another app with its access token in development mode
    please note that, if you want to make a comment and to be shown to the people you need a token with permissions associated with live app (meaning that you have to go through app review)

    This file is for commenter, deploy the code and get the url to register to the webhook (this should be done through live app)
'''

from flask import Flask, request ##################
from GCF_auto_private_reply import root
app = Flask(__name__) ####################

VERIFY_TOKEN = 'testbotverifytoken'

# this token is useless => we need it for webhook
# app: auto comment reply ==> page: Auto comment reply ==> accound: عمار ربيع
PAGE_TOKEN = "EAAHRZAzYWZCrcBACD9pXIgVct6Fy0DePEbHQU32unNcW4OLCymbKvYrkcxzZCgOS85S6Aiv6mz09fEtRrstZBz2oFYI2KbSwqa0zLhTsdkh2rOmTwpXZCOgLXxOgZBR9TZB31IZCCcRLsy85929YwQIts8CWRISKUv8vwBLUiWeniAZDZD"


# app: auto comment ==> page: Auto comment reply ==> accound: عمار ربيع
PAGE_TOKEN = "EAAcpGsFBqk0BAEU1haVb89h1JYvQEt6RvK0An7qdF7BrJmgYkWJubWJU2eAA1UZBjZCp8nyckZAeK4NqV2Ed01g6FKWZBbas5yHhassE4fqIOVjQCevMZCx5P3wOq4RBK74eaSpFJkB9ZCywXq41ee5UagP9qGVvYSAEOtZC9FADtjyTTjZClGUd"
PAGE_ID = "622508538161975" # Auto comment reply


@app.route("/", methods=["GET", "POST"])
def index():
    return root(request)
    

if __name__ == "__main__":
    app.run(debug=True)