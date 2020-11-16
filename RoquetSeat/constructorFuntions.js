function Celular(marcaCelular,tamanhoTela,capacidadeBateria) {
    this.marcaCelular = marcaCelular,
    this.tamanhoTela = tamanhoTela,
    this.capacidadeBateria = capacidadeBateria,
    this.ligar = function() {
        console.log('Fazendo Ligação...');
    }
}

const celular = new Celular('Apple', 6.0, 5000);
console.log(celular);
