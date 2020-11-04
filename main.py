from flask import Flask
import os

app = Flask(__name__)

environment = os.environ.get('env')

@app.route('/')
def hello():
    if environment == 'production':
        print('hola soy producción')
        return 'Hello World Production!'
    elif environment == 'development':
        print('hola soy desarrollo')
        return 'Hello World desarrollo!'

if __name__ == '__main__':
    app.run()