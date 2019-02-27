'''
    This file to run the server on you localhost --> you need ngrock or something like that to get a valid url discoved in the cloud
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