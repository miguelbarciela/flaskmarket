from market import app

#verifica si el archivo run.py se ejecutó directamente y no se importó
if __name__ == '__main__':
    app.run(debug=True)

