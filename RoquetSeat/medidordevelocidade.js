// Velocidade máxima até 70km
// A cada 5km acima do limite você ganha 1 ponto    
// Math.floor()
// Caso pontos maior de 12 -> "Carteira Suspensa"

verificarVelocidade(130);

function verificarVelocidade(Velocidade) {
    const velocidadeMaxima = 70;
    const kmPorPonto = 5;
    if (Velocidade <= velocidadeMaxima)
        console.log('Dentro da Velocidade Permitida!');
    else {
        const pontos = Math.floor((Velocidade - velocidadeMaxima) / kmPorPonto);
        if (pontos >= 12)
            console.log('Você atingiu o máximo de pontos permitido, Carteira Suspensa!');
        else
            console.log(`Velocidade Permitida Ultrapassada, Você recebeu ${pontos} Pontos `);
    }
}