function criarCelular(marcaCelular,tamanhoTela,capacidadeBateria) {
    return {
        marcaCelular,
        tamanhoTela,
        capacidadeBateria,
        ligar() {
            console.log('Fazendo Ligação...')
            }

       }
}

const celular1 = criarCelular('Motorola', 5.5, 5000)
console.log(celular1)
