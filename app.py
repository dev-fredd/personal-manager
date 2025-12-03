from flask import Flask, request, redirect, render_template
import json

app = Flask(__name__)

tareas = []
siguiente_id = 1


@app.route('/')
def index():
    cargar_datos()
    tareas_ordenadas = sorted(tareas, key=lambda x: x['completada'])
    return render_template('index.html', tareas=tareas_ordenadas)


def agregar_tarea(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'completada': False})
    siguiente_id += 1


def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
           tarea['completada'] = True
           guardar_datos()
           break

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
        guardar_datos()
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

def guardar_datos():
    with open('tareas.json', 'w') as f:
        json.dump({'siguiente_id':siguiente_id, 'tareas':tareas}, f)

def cargar_datos():
    global siguiente_id, tareas
    try:
        with open('tareas.json', 'r') as f:
            datos = json.load(f)
            tareas = datos['tareas']
            siguiente_id = datos['siguiente_id']
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    app.run(debug=True)