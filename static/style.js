function mostrarSenha(){

    let campo = document.getElementById("senha")

    if(campo.type === "password"){

        campo.type = "text"

    }else{

        campo.type = "password"

    }

}

const senha = document.querySelector("#senha")
const barra = document.querySelector("#barra")
const texto = document.querySelector("#texto")
const acoes = document.querySelector("#acoes")

senha.addEventListener("input", () => {

    let valor = senha.value

    let pontos = 0

    if(valor.length >= 8){
        pontos++
    }

    if(/[A-Z]/.test(valor)){
        pontos++
    }

    if(/[0-9]/.test(valor)){
        pontos++
    }

    if(/[!@#$%&*_-]/.test(valor)){
        pontos++
    }

    if(pontos <= 1){

        barra.style.width = "30%"
        barra.style.boxShadow =
    `0 0 20px ${barra.style.background}`

        texto.innerText = "Senha Fraca"

        acoes.classList.add("show")

    }

    else if(pontos <= 3){

        barra.style.width = "60%"
        barra.style.boxShadow =
    `0 0 20px ${barra.style.background}`

        texto.innerText = "Senha Média"

        acoes.classList.add("show")

    }

    else{

        barra.style.width = "100%"
       barra.style.boxShadow =
    `0 0 20px ${barra.style.background}`

        texto.innerText = "Senha Forte"

        acoes.classList.remove("show")

    }

})

async function gerarSenha(){

    const resposta = await fetch("/gerar_senha")

    const dados = await resposta.json()

    senha.value = dados.senha

    senha.dispatchEvent(new Event("input"))

    mostrarToast("Senha Forte Gerada!")
}
function mostrarToast(msg){

    const toast = document.getElementById("toast")

    toast.innerText = msg

    toast.classList.add("show")

    setTimeout(() => {

        toast.classList.remove("show")

    }, 3000)

}

function trocarSenha(){
    senha.value = ""

    barra.style.width = "0%"

    texto.innerText = ""

    acoes.classList.remove("show")

    mostrarToast("Digite uma nova senha")
}