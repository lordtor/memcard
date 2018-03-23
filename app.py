import os
from flask import Flask
app = Flask(__name__)

app = Flask(__name__)
app.config.from_object('config.StagingConfig')
#config.StagingConfig
#config.ProductionConfig

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()