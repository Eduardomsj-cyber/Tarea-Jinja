from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la peticion")

@app.after_request
def after_request(response):
    print("despues de la peticion")
    return response

@app.route('/')
def index():

    # lista
    #las listas llevan [] por eso el error
    cursos = ['PHP', 'PYTHON', 'JAVA', 'KOTLIN', 'DART', 'JAVASCRIPT']

    # diccionario
    data = {
        'titulo': 'Index',
        'Bienvenida': '!Saludos!',
        'Motor': 'Estamos usando la librería jinja para esta lista',
        'cursos': cursos,
        # Número de cursos de la lista
        'numero_cursos': len(cursos)
    }

    return render_template('index.html', data=data)

#url personalizada
#URL DINAMICA
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data={
            'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad

    }
    return render_template('contacto.html', data= data)

#query string

def query_string():
    print (request)
    print (request.args)
    print (request.args.get('param1'))
    print (request.args.get('param2'))

    return "ok"

#Pagina no encontrada

def pagina_no_encontrada(error):
   #Redirije ala pagina para evitar el error 404
   return redirect(url_for('index'))



if __name__ == '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=9090)
