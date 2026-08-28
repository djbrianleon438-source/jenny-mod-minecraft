# build 97fd809153
# (auto) 9f3f6a
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
