from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('dkdkdkkd')
    return "hello, world.<br>kdkdkdk"
    # return 'Hello, World!'
