const express = require('express');
const app = express();
const data = require('./data.json')

app.use(express.json());

app.get("/clients", function (require, response){
    response.json(data);
});

app.get("/clients/:id", function (require, response){
    const { id } = require.params;
    const client = data.find(cli = cli.id == id);

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
    const client = data.find(cli = cli.id == id);

    if (!client) return response.status(204).json();

    const { name } = require.body;

    client.name = name;

    response.json(client);
});
app.delete("/clients/:id", function (require, response){
    const { id } = require.params;
    const clientesFiltered = data.filter(cliente => client.id != id);

    response.json(clientesFiltered);
})


app.listen(3000, function () {
    console.log('Server is running');
});