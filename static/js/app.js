<<<<<<< HEAD
const cep = document.getElementById("cep");

cep.addEventListener("input", function () {
    let valor = this.value.replace(/\D/g, "");

    if (valor.length > 8) {
        valor = valor.substring(0, 8);
    }

    if (valor.length > 5) {
        valor = valor.substring(0, 5) + "-" + valor.substring(5);
    }

    this.value = valor;
});

cep.addEventListener("blur", consultarCEP);

async function consultarCEP() {

    const valor = cep.value.replace(/\D/g, "");

    if (valor.length !== 8) {
        return;
    }

    try {

        const resposta = await fetch(
            `https://viacep.com.br/ws/${valor}/json/`
        );

        if (!resposta.ok) {
            throw new Error("Erro na conexão com o ViaCEP");
        }

        const endereco = await resposta.json();

        if (endereco.erro) {
            alert("CEP não encontrado.");
            return;
        }

        document.getElementById("logradouro").value =
            endereco.logradouro || "";

        document.getElementById("bairro").value =
            endereco.bairro || "";

        document.getElementById("cidade").value =
            endereco.localidade || "";

        document.getElementById("estado").value =
            endereco.uf || "";

        document.getElementById("regiao").value =
            endereco.regiao || "";

    } catch (erro) {

        console.error("Erro:", erro);

        alert("Não foi possível consultar o CEP.");
    }
};


document.getElementById("salvar").addEventListener("click", function () {

    const dados = {
        cep: document.getElementById("cep").value,
        logradouro: document.getElementById("logradouro").value,
        bairro: document.getElementById("bairro").value,
        cidade: document.getElementById("cidade").value,
        estado: document.getElementById("estado").value,
        regiao: document.getElementById("regiao").value,
        numero: document.getElementById("numero").value
    };

    localStorage.setItem(
        "endereco",
        JSON.stringify(dados)
    );

    document.getElementById("mensagem").textContent =
        "Informações salvas!";
});


document.getElementById("limpar").addEventListener("click", function () {

    localStorage.removeItem("endereco");

    document.getElementById("formEndereco").reset();

    document.getElementById("mensagem").textContent =
        "Informações apagadas!";
});


window.addEventListener("load", function () {

    const dadosSalvos = localStorage.getItem("endereco");

    if (!dadosSalvos) {
        return;
    }

    const dados = JSON.parse(dadosSalvos);

    document.getElementById("cep").value = dados.cep || "";
    document.getElementById("logradouro").value = dados.logradouro || "";
    document.getElementById("bairro").value = dados.bairro || "";
    document.getElementById("cidade").value = dados.cidade || "";
    document.getElementById("estado").value = dados.estado || "";
    document.getElementById("regiao").value = dados.regiao || "";
    document.getElementById("numero").value = dados.numero || "";
});


document.getElementById("cadastrar").addEventListener("click", async function () {

    const dados = {
        cep: document.getElementById("cep").value,
        logradouro: document.getElementById("logradouro").value,
        bairro: document.getElementById("bairro").value,
        cidade: document.getElementById("cidade").value,
        estado: document.getElementById("estado").value,
        regiao: document.getElementById("regiao").value,
        numero: document.getElementById("numero").value
    };

    try {

        const resposta = await fetch("/cadastrar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        document.getElementById("mensagem").textContent =
            resultado.mensagem;

    } catch (erro) {

        console.error(erro);

        document.getElementById("mensagem").textContent =
            "Erro ao conectar com o servidor.";
    }
});
=======
document.getElementById("cep").addEventListener("blur", buscarCEP);

async function buscarCEP() {

    const cep = document.getElementById("cep").value;

    if (cep == "") return;

    try {

        const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);

        const dados = await resposta.json();

        document.getElementById("logradouro").value = dados.logradouro;
        document.getElementById("bairro").value = dados.bairro;
        document.getElementById("cidade").value = dados.localidade;
        document.getElementById("estado").value = dados.uf;
        document.getElementById("regiao").value = dados.regiao;

    }

    catch (erro){

        alert("CEP inválido.");

    }

}
>>>>>>> ad2e2e4386f0187402597929d3ef16a56e46293d
