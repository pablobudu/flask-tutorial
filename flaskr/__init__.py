import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test |config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Añado las funciones para cerrar la BD y para añadir la función de la línea de comandos acá, para que se añadan a la aplicación creada. 
    from . import db 
    db.init_app(app); #Acá llamo a la función que efectivamente añade dichas funciones.

    #Se añaden las "Blueprints" a la iniciación de la aplicación
    from . import auth
    app.register_blueprint(auth.bp)
    return app
