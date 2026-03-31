from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Página de Inicio</h1><p>Bienvenido a la aplicación Flask.</p>'

@app.route('/acerca-de')
def acerca_de():
    return '<h1>Acerca de</h1><p>Información sobre nosotros.</p>'

@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h1><p>Formulario de contacto.</p>'

if __name__ == '__main__':
    app.run(debug=True)