from flask import Flask, render_template, request, redirect, url_for, abort, session 
app = Flask("__name__") 
#------------------------Rutas de Acceso--------------------------------------#
@app.route('/') 
def home(): 
	return render_template('index.html')
@app.route('/table', methods=['POST'])
def tabla():
        nombre=request.form['name']
        return render_template('tabla.html')
@app.route('/instalacion')
def instalacion():
        return render_template('instalacion.html')
@app.route('/sml')
def sml():
        return render_template('sml.html')
@app.route('/python')
def python():
        return render_template('python.html')
#--------------------------- MAIN --------------------------------------------#
if __name__ == '__main__': 
	app.run(debug=True, use_debugger=True, use_reloader=True)
