from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
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


if __name__ == "__main__":
    app.run(debug=True)