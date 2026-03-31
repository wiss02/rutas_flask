from flask import Flask

app = Flask(__name__)

# Obliga a que la edad sea un número entero (int)
@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'<h1>Tienes {edad} años.</h1>'

# Obliga a que el valor sea un número decimal (float)
@app.route('/precio/<float:valor>')
def mostrar_precio(valor):
    return f'<h1>El precio del artículo es: ${valor}</h1>'

if __name__ == '__main__':
    app.run(debug=True)