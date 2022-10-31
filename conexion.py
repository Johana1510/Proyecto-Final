
from distutils.util import execute
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "johana12"
app.config["MYSQL_DB"] = "proyecto"
mysql=MySQL(app)

app.secret_key = "johanaproyectofinal"

@app.route("/")
def index():
    return render_template("registrarse.html")

app.route("Add_proyecto", methods=["POST"])
def add_user():
    if request.method =="POST":
        usuario = request.form["usuario"]
        correo_electronico = request.form["correo_electronico"]
        contraseña = request.form["contraseña"]
        confirmar_contraseña = request.form["confirmar_contraseña"]
        cur = mysql.connection.cursor()
        cur = execute("INSERT INTO proyecto(usuario,correo_electronico,contraseña,confirmar_contraseña)VALUES(%s,%s,%s,%s)",
        (usuario,correo_electronico,contraseña,confirmar_contraseña))
        mysql.connection.commit()
        flash("proyecto Added successfully")
        return redirect(url_for(index))

if __name__ == "__main__":
    app.run(debug=True)
    

