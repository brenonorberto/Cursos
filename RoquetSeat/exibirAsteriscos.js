// Criar uma função de exibe a quantidade de * que a linha possui

exibirAsteriscos(20);

function exibirAsteriscos(linhas) {
    let padrao = '';
    for(let linha = 1; linha <= linhas; linha++) {
        padrao += '*';
        console.log(padrao);
    }
}