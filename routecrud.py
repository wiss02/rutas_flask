from flask import Flask

app = Flask(__name__)

@app.route('/api/recurso', methods=['GET'])
def leer_recurso():
    return '<h1>Leer (GET): Obteniendo todos los recursos.</h1>'

@app.route('/api/recurso', methods=['POST'])
def crear_recurso():
    return '<h1>Crear (POST): Recurso creado exitosamente.</h1>'

@app.route('/api/recurso/<int:id>', methods=['PUT'])
def actualizar_recurso(id):
    return f'<h1>Actualizar (PUT): Recurso {id} actualizado.</h1>'

@app.route('/api/recurso/<int:id>', methods=['DELETE'])
def eliminar_recurso(id):
    return f'<h1>Eliminar (DELETE): Recurso {id} eliminado.</h1>'

if __name__ == '__main__':
    app.run(debug=True)