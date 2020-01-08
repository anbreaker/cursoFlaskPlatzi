from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

toDos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.route('/')
def index():
    userIp = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('userIp', userIp)

    return response

# decorador de python
@app.route('/hello')
def hello():
    userIp = request.cookies.get('userIp')
    context = {
        'userIp': userIp,
        'toDos': toDos
    }

    # return f'Hello world Flask tu ip es: {userIp}'
    return render_template('/hello.html', **context)
