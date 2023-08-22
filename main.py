from flask import Flask, render_template,request
from BD_Usuarios import lista_Usuarios
app = Flask(__name__)


@app.route("/")
def homepage():
  return render_template("homepage.html")
@app.route("/Usuarios",methods=['GET'])

@app.route("/lista_usuarios",methods=['GET'])
def get_Usuarios():
  return lista_Usuarios


@app.route('/Login')
def Login():
    return render_template('Login.html')
@app.route('/autenticar',methods=['POST'])
def autenticar():
    Cpf = request.form.get('cpf')
    usuario =request.form.get('usuario')
    Nascimento = request.form.get('nascimento')
    lista_Usuarios.append([Cpf,Nascimento,usuario])
    return "Sucesso! Usuario : {}   CPF: {}    Data de Nascimento: {}".format(usuario,Cpf,Nascimento)

if __name__=="__main__":
  app.run(debug=True)
