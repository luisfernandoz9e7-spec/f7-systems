import os
from flask import Flask, render_template

# Configura las rutas absolutas para que Flask encuentre la carpeta templates y static sin errores
template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)