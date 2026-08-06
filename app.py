from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",     
    database="enderecos"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    cep = request.form["cep"]
    logradouro = request.form["logradouro"]
    bairro = request.form["bairro"]
    cidade = request.form["cidade"]
    estado = request.form["estado"]
    regiao = request.form["regiao"]
    numero = request.form["numero"]

    cursor = conexao.cursor()

    sql = """
    INSERT INTO endereco
    (cep, logradouro, bairro, cidade, estado, regiao, numero)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    valores = (
        cep,
        logradouro,
        bairro,
        cidade,
        estado,
        regiao,
        numero
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()

    return """
    <h2>Cadastro realizado com sucesso!</h2>
    <a href="/">Voltar</a>
    """

if __name__ == "__main__":
    app.run(debug=True)