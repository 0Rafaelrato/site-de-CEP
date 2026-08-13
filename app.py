<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
=======
from flask import Flask, render_template, request
>>>>>>> ad2e2e4386f0187402597929d3ef16a56e46293d
import mysql.connector

app = Flask(__name__)

<<<<<<< HEAD

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="enderecos"
    )

=======
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",     
    database="enderecos"
)
>>>>>>> ad2e2e4386f0187402597929d3ef16a56e46293d

@app.route("/")
def index():
    return render_template("index.html")

<<<<<<< HEAD

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    try:

        banco = conectar()
        cursor = banco.cursor()

        sql = """
        INSERT INTO endereco
        (cep, logradouro, bairro, cidade, estado, regiao, numero)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            dados["cep"],
            dados["logradouro"],
            dados["bairro"],
            dados["cidade"],
            dados["estado"],
            dados["regiao"],
            dados["numero"]
        )

        cursor.execute(sql, valores)

        banco.commit()

        cursor.close()
        banco.close()

        return jsonify({
            "mensagem": "Endereço cadastrado no MySQL!"
        })

    except Exception as erro:

        print(erro)

        return jsonify({
            "mensagem": "Erro ao cadastrar no MySQL."
        }), 500

=======
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
>>>>>>> ad2e2e4386f0187402597929d3ef16a56e46293d

if __name__ == "__main__":
    app.run(debug=True)