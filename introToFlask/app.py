from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

#view function: represent a html page
#single forward slash is the root url
@app.route('/')
def hello():
    return "Hello World"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)