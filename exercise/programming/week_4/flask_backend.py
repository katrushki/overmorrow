from flask import Flask

app = Flask(__name__)

def index():
    return 'I solemnly swear I am up to no good'