let amigo = {nome: 'Breno', 
sexo: 'M', 
peso: 75, 
engordar(p){
    console.log('Engordou!')
    this.peso += p
} }
amigo.engordar(2)
console.log(`${amigo.nome} pesa ${amigo.peso}Kg`)