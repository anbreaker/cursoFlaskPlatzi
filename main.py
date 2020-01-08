from flask import Flask, request

app = Flask(__name__)

#decorador de python
@app.route('/')
def hello():
    userIp = request.remote_addr
    return f'Hello world Flask tu ip es: {userIp}'