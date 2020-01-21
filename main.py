from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

toDos = ['Tarea 1', 'Tarea 2', 'Tarea 3']


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
