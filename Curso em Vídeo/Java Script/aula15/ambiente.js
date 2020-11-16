let num = [5, 8, 2, 9, 3]
num.push(1) // adicionar valor
num.sort() // colocar em ordem crescente
console.log(num)
console.log(`O valor tem ${num.length} posições!`)
console.log(`O primeiro valor do vetor ${num[0]}`)
let pos = num.indexOf(10)
if (pos == -1) {
    console.log('Valor não existe!')
} else {
    console.log(`Valor está na posição ${pos}`)
}
