// Criar um metodo para ler propriedades de um objeto
// Exibir somente as propriedades do tipo string que estão nesse objeto

const filme = {
    titulo: 'Vingadores',
    ano: 2018,
    direto: 'Robin',
    personagem: 'Thor'
    }

exibePropriedades(filme);

function exibePropriedades(obj){
    for (prop in obj)
    if (typeof obj[prop] === 'string')
    console.log(`${prop}: ${obj[prop]}`)
    }