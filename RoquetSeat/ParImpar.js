// Receber uma quantidade de valores para avaliar
// Função exibe se o número é Par ou Impar.
exibirTipo(12);
function exibirTipo(limite){
    for (let i = 0; i <= limite; i++) {
        if (i % 2 == 0)
            console.log(i,'Número Par')
        else
            console.log(i,'Número Impar')
    }
}