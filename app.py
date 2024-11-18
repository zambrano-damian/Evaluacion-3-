from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    if request.method == 'POST':
        # Obtener las notas y la asistencia
        notas = [int(request.form['nota1']), int(request.form['nota2']), int(request.form['nota3'])]
        asistencia = int(request.form['asistencia'])

        promedio = sum(notas) / len(notas)
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

        return render_template('form1.html', promedio=promedio, estado=estado)
    return render_template('form1.html')

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    if request.method == 'POST':
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        return render_template('form2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)
