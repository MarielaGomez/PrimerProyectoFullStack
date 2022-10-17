from flask import Flask,  render_template, request, redirect, url_for, flash, session # pip install Flask
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL # pip install Flask-MySQLdb
from flask_wtf.csrf import CSRFProtect
from os import path #pip install notify-py
from notifypy import Notify
from flask_login import LoginManager, login_user, logout_user, login_required# solo ingreso on usuario logeado
from config import config
from flask_login import LoginManager
import controlador
import avatar
import contacto






# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

#proteccion token
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

#almacenar todos los datos de el usuario
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)



@app.route('/')
def index():
    return render_template('contenido.html')


# login ---------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #se crea user = clase user, 0 por id que no lo tengo, se ingresa usuario y pass del formulario
        user = User(0, request.form['username'], request.form['password'])
        #se grea variable logged_user = que es igual a lo que retorne ModelUser en su metodo login (con los parametros de la base de datos )
        logged_user = ModelUser.login(db, user)
                
        if logged_user != None: # existe el usuario? 
            if logged_user.password: # comparar si el password coincide o no. es true?
                login_user(logged_user) #login_user impostada con logeed_user, para que almacene el usuario logueado
                return redirect(url_for('home'))
            else:
                flash("Password incorrecto ...")
                return render_template('auth/login.html')
        else:
            flash("Ususario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
#----------------------Contacto-----------------------
@app.route("/ingresoContacto")
def ingresoContacto():
    return render_template("contacto.html")



@app.route("/envioContacto", methods=["POST"])
def envioContacto():
    ingreso_asunto = request.form["asunto"]
    ingreso_cuerpo = request.form["cuerpo"]
    
    contacto.contacto(ingreso_asunto, ingreso_cuerpo)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/home")
#---------------------------------------------


@app.route('/registro', methods = ["GET", "POST"])
def registro():
    
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM tip_usu")
        tipo = cur.fetchall()

        cur = db.connection.cursor()
        cur.execute("SELECT * FROM level")
        level = cur.fetchall()        

        cur.close()

        notificacion = Notify()
        
        

        if request.method == 'GET':
            return render_template("registro.html", tipo = tipo, level = level )
        #--------------
        user = User(0, request.form['name'], request.form['password'])
        #se genera variable logged_user = que es igual a lo que retorne ModelUser en su metodo login (con los parametros de la base de datos )
        logged_user = ModelUser.login(db, user)
        if logged_user == None: # existe el usuario? 
            username = request.form['name']
            email = request.form['email']
            password = generate_password_hash(request.form['password'])
            tipo = request.form['tipo']
            level = request.form['level']

            cur = db.connection.cursor()
            cur.execute("INSERT INTO user (username, email, password, id_lev_usu, tipo) VALUES (%s,%s,%s,%s,%s)", (username, email, password, level ,tipo,))
            db.connection.commit()
            notificacion.title = "Registro Exitoso"
            notificacion.message="ya te encuentras registrado."
            notificacion.send()
            return redirect(url_for('login'))
            
        else:
            flash("El usuario ya esta en uso, elegir otro...")
            return render_template("registro.html", tipo = tipo, level = level )
        
        
                    
        #--------------
        
            


    
#---------------------------------------------
@app.route("/agregar_usuario")
def formulario_agregar_datos():
    return render_template("agregar_usuario.html")

@app.route("/config_usuario")
def configurar_usuario():
    return render_template("config_usuario.html")


@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador.insertar_usuario(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuarios")



@app.route("/usuarios")
def datos():
    datos = controlador.obtener_usuarios()
    return render_template("usuarios.html", datos=datos)


@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador.eliminar_usuario(request.form["id"])
    return redirect("/usuarios")


@app.route("/editar_usuario", methods=["POST"])
@login_required
def editar_usuario():
    
    
    datos = controlador.obtener_usuario_por_id(request.form["id"])
    return render_template("editar_usuario.html", datos=datos)

#-----------------------Generador de avatar ---

@app.route("/generar_avatar", methods=["POST"])
@login_required
def generar_avatar():
    avatar.avatar_generador(request.form["id"])
    
    
    return redirect("/config_usuario")
#---------------------------------




@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id = request.form["id"]
    username = request.form["username"]
    dni = request.form["dni"]
    email = request.form["email"]
    nombres = request.form["nombres"]
    apellido = request.form["apellido"]
    direccion = request.form["direccion"]
    numeracion = request.form["numeracion"]

    controlador.actualizar_usuario(username, dni, email, nombres, apellido, direccion, numeracion, id)
    return redirect("/config_usuario")




#---------------------------------------------

@app.route('/logout')
def logout():
    logout_user()
    return render_template('contenido.html')

@app.route('/home')
@login_required
def home():
    return render_template('premium/index.html')

@app.route('/premium')
def premium():
    logout_user()
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404




if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app) #proteccuion token
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)    
    #app.run()
    app.debug = True
    app.run(host= '0.0.0.0', port= 82)
    #print (SSL._CERTIFICATE_PATH_LOCATIONS)
