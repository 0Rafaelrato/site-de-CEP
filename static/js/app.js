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