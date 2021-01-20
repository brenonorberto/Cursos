const express = require('express'); // Chamando express
const app = express(); // instanciando ma variável app
const data = require('./data.json')

app.use(express.json()); //Avisar o express para usar json

/* 
URI
http://localhost:3000/clients

Endpoint
clients
*/

// Verbos HTTP
app.get("/clients", function (require, response){
    response.json(data);
});

app.get("/clients/:id", function (require, response){
    const { id } = require.params;
    const client = data.find(cli => cli.id == id);

    if (!client) return response.status(204).json();

    response.json(client);
});

app.post("/clients", function (require, response){
    const { name, email } = require.body;

    //Salvar

    response.json({name, email});
});

app.put("/clients/:id", function (require, response){
    const { id } = require.params;
    const client = data.find(cli => cli.id == id);

    if (!client) return response.status(204).json();

    const { name } = require.body;

    client.name = name;

    response.json(client);
});
app.delete("/clients/:id", function (require, response){
    const { id } = require.params;
    const clientesFiltered = data.filter(client => client.id != id);

    response.json(clientesFiltered);
})

//Iniciando servidor
app.listen(3000, function () {
    console.log('Server is running');
});