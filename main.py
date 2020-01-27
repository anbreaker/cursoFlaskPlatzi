from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)

#Configuracion segura de la app flask
app.config['SECRET_KEY'] = 'SUPER SECRETO'

toDos = ['Tarea 1', 'Tarea 2', 'Tarea 3']


@app.errorhandler(404)
def notFound(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def serverError5XX(error):
    #Para provocar error 500, export FLASK_DEBUG=0
    #Comentar return @app.route('/')
    return render_template('500.html', error=error)

@app.route('/')
def index():
    userIp = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('userIp', userIp)
    session['userIp']= userIp

    return response 


# decorador de python
@app.route('/hello')
def hello():
    # userIp = request.cookies.get('userIp')
    userIp = session.get('userIp')
    context = {
        'userIp': userIp,
        'toDos': toDos
    }

    # return f'Hello world Flask tu ip es: {userIp}'
    return render_template('/hello.html', **context)
