CREATE DATABASE IF NOT EXISTS enderecos;

USE enderecos;

CREATE TABLE IF NOT EXISTS endereco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cep VARCHAR(9) NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    regiao VARCHAR(100) NOT NULL,
    numero INT NOT NULL
);

ALTER USER 'nome_do_usuario'@'localhost' IDENTIFIED BY 'nova_senha'; FLUSH PRIVILEGES;

isso e para criar a tabela no sql e trocar senha se não trocar senha não da certo.
Trocar o "nome_do_usuario" por o seu nome de usuario que colocou no py
Trocar tbm o "nova_senha" por sua senha que colocou no py