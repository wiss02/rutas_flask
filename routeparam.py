from flask import Flask

app = Flask(__name__)

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'<h1>Hola, {nombre}!</h1><p>Este es tu perfil.</p>'

@app.route('/categoria/<categoria>/<producto>')
def mostrar_producto(categoria, producto):
    return f'<h1>Categoría: {categoria}</h1><h2>Producto: {producto}</h2>'

if __name__ == '__main__':
    app.run(debug=True)